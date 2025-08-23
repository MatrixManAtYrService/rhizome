import asyncio

import structlog
from pydantic import BaseModel


class NewProcessResponse(BaseModel):
    status: str
    pid: int


class ProcessInfo(BaseModel):
    pid: int


class ProcessListResponse(BaseModel):
    running: list[ProcessInfo]
    count: int


class ProcessManager:
    """Generic manager for async subprocesses and their output streaming."""

    def __init__(self) -> None:
        # Set to track running async processes
        self._processes: set[asyncio.subprocess.Process] = set()
        # Set to track async tasks for process output streaming
        self._output_tasks: set[asyncio.Task[None]] = set()

    async def _stream_stdout(self, process: asyncio.subprocess.Process, logger: structlog.stdlib.BoundLogger) -> None:
        """Stream stdout from process."""
        if process.stdout is None:
            return
        try:
            while True:
                line = await process.stdout.readline()
                if not line:
                    break
                decoded_line = line.decode().rstrip()
                if decoded_line:  # Only log non-empty lines
                    logger.info(decoded_line, file="stdout")
        except Exception as e:
            logger.error("Error streaming stdout", error=str(e))

    async def _stream_stderr(self, process: asyncio.subprocess.Process, logger: structlog.stdlib.BoundLogger) -> None:
        """Stream stderr from process."""
        if process.stderr is None:
            return
        try:
            while True:
                line = await process.stderr.readline()
                if not line:
                    break
                decoded_line = line.decode().rstrip()
                if decoded_line:  # Only log non-empty lines
                    logger.info(decoded_line, file="stderr")
        except Exception as e:
            logger.error("Error streaming stderr", error=str(e))

    async def stream_process_output(self, process: asyncio.subprocess.Process, pid: int, process_name: str) -> None:
        """Stream process output line by line and log it with structlog."""
        # Use a logger with the process name instead of module name
        process_logger = structlog.get_logger(process_name).bind(pid=pid)

        if process.stdout is None and process.stderr is None:
            process_logger.warning("No stdout or stderr available for process")
            return

        try:
            # Stream both stdout and stderr concurrently
            await asyncio.gather(
                self._stream_stdout(process, process_logger),
                self._stream_stderr(process, process_logger),
                return_exceptions=True,
            )
        except Exception as e:
            process_logger.error("Error in output streaming", error=str(e))
        finally:
            # Wait for process to finish and remove from tracking
            await process.wait()
            self._processes.discard(process)
            process_logger.info(f"subprocess finished with return code {process.returncode}")

    async def start_process(self, args: list[str], process_name: str) -> NewProcessResponse:
        """Start a generic async subprocess with output streaming."""
        # Start async subprocess
        process = await asyncio.create_subprocess_exec(
            *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        # Add to our tracking set
        self._processes.add(process)

        # Start async task to stream output with process name
        task = asyncio.create_task(self.stream_process_output(process, process.pid, process_name))
        self._output_tasks.add(task)

        # Clean up completed tasks
        task.add_done_callback(self._output_tasks.discard)

        # Log with process name instead of module name
        process_logger = structlog.get_logger(process_name).bind(pid=process.pid)
        process_logger.info("subprocess started")

        return NewProcessResponse(status="started", pid=process.pid)

    def list_processes(self) -> ProcessListResponse:
        """List running processes."""
        # Clean up completed processes
        completed = {p for p in self._processes if p.returncode is not None}
        self._processes.difference_update(completed)

        # Return list of running processes
        running = [ProcessInfo(pid=p.pid) for p in self._processes]

        return ProcessListResponse(running=running, count=len(running))

    async def cleanup(self) -> None:
        """Clean up all running processes and tasks."""
        # Cancel all output streaming tasks
        for task in self._output_tasks:
            task.cancel()

        # Terminate any remaining processes
        for process in self._processes:
            if process.returncode is None:  # Still running
                process.terminate()


# Global process manager instance
process_manager = ProcessManager()
