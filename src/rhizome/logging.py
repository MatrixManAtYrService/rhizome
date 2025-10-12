import logging

import structlog


class FilterLoggingEndpoints(logging.Filter):
    """Filter to exclude access logs for logging endpoints."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Return False to filter out logging endpoint requests."""
        message = record.getMessage()
        # Filter out POST requests to logging endpoints
        return not any(
            endpoint in message for endpoint in ["/log_query", "/log_query_result", "/log_request", "/log_response"]
        )


def setup_logging() -> None:
    """Set up unified logging through structlog."""
    # Shared processors for both structlog and standard logging
    shared_processors = [
        structlog.stdlib.add_logger_name,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="%H:%M:%S"),
        structlog.processors.StackInfoRenderer(),
    ]

    # Configure structlog
    structlog.configure(
        processors=shared_processors
        + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # Create formatter using structlog with wider message field
    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            structlog.dev.ConsoleRenderer(pad_event=40),
        ],
    )

    # Set up handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    # Set up a simple formatter for verbose external libraries
    simple_formatter = logging.Formatter("%(asctime)s %(message)s", datefmt="%H:%M:%S")
    simple_handler = logging.StreamHandler()
    simple_handler.setFormatter(simple_formatter)

    # Configure specific loggers to use simple formatting or prevent duplicate logging
    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"):
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.propagate = False
        logger.addHandler(simple_handler)
        logger.setLevel(logging.INFO)

    # Add filter to uvicorn.access to hide logging endpoint requests
    access_logger = logging.getLogger("uvicorn.access")
    access_logger.addFilter(FilterLoggingEndpoints())

    # Configure httpx to use simple formatting (it has very verbose messages)
    httpx_logger = logging.getLogger("httpx")
    httpx_logger.handlers.clear()
    httpx_logger.propagate = False
    httpx_logger.addHandler(simple_handler)
    httpx_logger.setLevel(logging.INFO)
