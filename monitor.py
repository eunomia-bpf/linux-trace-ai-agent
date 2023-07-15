import csv
import subprocess
import psutil
import time

import psutil
import csv
import time

def monitor(pid: int):
    """
    Monitors the specified process identified by its PID and records its CPU usage, memory usage,
    I/O read/write bytes, and network connections to a CSV file.

    Args:
        pid (int): The process ID (PID) of the process to monitor.

    Returns:
        None
    """

    process = psutil.Process(pid)

    sampling_duration = 1  # Sampling duration in seconds
    sampling_interval = 0.01

    fieldnames = ['Time', 'CPU Usage', 'Memory Usage', 'IO Read Bytes', 'IO Write Bytes', 'Network Connections']

    with open('trace.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        start_time = time.time()
        end_time = start_time + sampling_duration

        while time.time() < end_time:
            cpu_percent = process.cpu_percent(interval=None)
            memory_info = process.memory_info()
            io_counters = process.io_counters()
            connections = process.connections()
            writer.writerow({
                'Time': time.time(),
                'CPU Usage': cpu_percent,
                'Memory Usage': memory_info.rss,
                'IO Read Bytes': io_counters.read_bytes,
                'IO Write Bytes': io_counters.write_bytes,
                'Network Connections': len(connections)
            })

            time.sleep(sampling_interval)

    