import psutil
import subprocess
import re


def execute(execute_string):
    output = subprocess.run(
        execute_string,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return output

def get_memory_usage(pid):
    try:
        # Get process info using PID
        process = psutil.Process(pid)
        # Get memory info
        memory_info = process.memory_info()
        memory_usage_bytes = memory_info.rss
        if memory_usage_bytes is not None:
            # Convert bytes to megabytes for better readability (optional)
            memory_usage_mb = memory_usage_bytes / (1024 * 1024)
            return memory_usage_mb
            # print(f"Process (PID {pid}) memory usage: {memory_usage_mb:.2f} MB")

    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        return None



def get_processes_by_pattern(pattern):
    """
    Searches for running processes matching a pattern and returns their information.

    Args:
        pattern (str): A regular expression pattern to match process names.

    Returns:
        list: A list of dictionaries containing information about matching processes.
    """
    matching_processes = []
    for proc in psutil.process_iter(["pid", "name", "status"]):
        if re.search(pattern, proc.info("name")):
            try:
                matching_processes.append(
                    proc.as_dict(
                        attrs=["pid", "name", "status", "cpu_percent", "memory_percent"]
                    )
                )
            except psutil.NoSuchProcess:
                # Process might have disappeared between checks
                pass
    return matching_processes


