import asyncio
from typing import Any

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
    
    async def stream_process_output(self, process: asyncio.subprocess.Process, pid: int, process_name: str) -> None:
        """Stream process output line by line and log it with structlog."""
        # Use a logger with the process name instead of module name
        process_logger = structlog.get_logger(process_name).bind(pid=pid)
        
        if process.stdout is None:
            process_logger.warning("No stdout available for process")
            return
        
        try:
            # Read lines from stdout asynchronously
            while True:
                line = await process.stdout.readline()
                if not line:
                    # Process has finished
                    break
                    
                # Log the output line (strip newline) as the message itself
                decoded_line = line.decode().rstrip()
                process_logger.info(decoded_line)
                
        except Exception as e:
            process_logger.error("Error streaming output", error=str(e))
        finally:
            # Wait for process to finish and remove from tracking
            await process.wait()
            self._processes.discard(process)
            process_logger.info("subprocess finished")
    
    async def start_process(self, args: list[str], process_name: str) -> NewProcessResponse:
        """Start a generic async subprocess with output streaming."""
        # Start async subprocess
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
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
        
        return NewProcessResponse(
            status="started",
            pid=process.pid
        )
    
    def list_processes(self) -> ProcessListResponse:
        """List running processes."""
        # Clean up completed processes
        completed = {p for p in self._processes if p.returncode is not None}
        self._processes.difference_update(completed)
        
        # Return list of running processes
        running = [ProcessInfo(pid=p.pid) for p in self._processes if p.pid is not None]
        
        return ProcessListResponse(
            running=running,
            count=len(running)
        )
    
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