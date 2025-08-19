"""
Sleeper subprocess - A test implementation for rhizome process management.

This module exists purely for testing rhizome's ability to manage long-running
subprocesses and stream their output. The actual use case for rhizome is to manage
processes like "kubectl port-forward" that need to run continuously in the background.

The sleeper process simply prints numbers 0-4 with a configurable sleep interval,
allowing us to verify that:
- Processes start correctly and return immediately
- Output is streamed in real-time
- Process tracking works (/ps endpoint)
- Cleanup happens when processes finish
"""

import os
import sys

from rhizome.proc import NewProcessResponse, process_manager


async def start_sleeper(iterations: int = 5) -> NewProcessResponse:
    """
    Start a sleeper subprocess for testing rhizome process management.

    This is a test subprocess that prints numbers with configurable sleep.
    The real use case will be managing kubectl port-forward processes.

    Args:
        iterations: Number of times to print and sleep (default: 5)
    """
    sleep_duration = os.environ.get("SLEEP_OVERRIDE", "1")
    process_name = "sleeper"

    # Python code to run in subprocess - this simulates a long-running process
    python_code = f"""
from time import sleep
for i in range({iterations}):
    print(i, flush=True)
    sleep({sleep_duration})
"""

    # Build command args for the generic process manager
    args = [sys.executable, "-c", python_code]

    # Use the generic process manager to start the process
    return await process_manager.start_process(args, process_name)


# Legacy function for backward compatibility (no parameters)
async def start_sleeper_legacy() -> NewProcessResponse:
    """Legacy start_sleeper function for testing compatibility."""
    return await start_sleeper(iterations=5)
