import time
import psutil
from pydantic import BaseModel, Field

def sample(pid: int):
    """
    Monitors the specified process identified by its PID and records its CPU usage, memory usage,
    I/O read/write bytes, and network connections.
    Args:
        pid (int): The process ID of the process to monitor.

    Returns:
        The `sample` function returns a dictionary that contains recorded metrics for 
        the monitored process, including CPU usage percentages, memory usage values (in bytes), 
        I/O read and write bytes, and the number of network connections within 2.5 seconds.
    """
    process = psutil.Process(pid)

    records = {
        "CPU Usage": [],
        "Memory Usage": [],
        "IO Read Bytes": [],
        "IO Write Bytes": [],
        "Network Connections": []
    }

    for _ in range(50):
        cpu_percent = process.cpu_percent(interval=0.1)
        memory_info = process.memory_info()
        io_counters = process.io_counters()
        connections = process.connections()
        records['CPU Usage'].append(cpu_percent)
        records['Memory Usage'].append(memory_info.rss)
        records['IO Read Bytes'].append(io_counters.read_bytes)
        records['IO Write Bytes'].append(io_counters.write_bytes)
        records['Network Connections'].append(len(connections))
        time.sleep(0.05)
    return records


class SampleInput(BaseModel):
    pid: int = Field(
        ...,
        description="The process ID (PID) of the process to monitor.",
        example="5478",
    )
