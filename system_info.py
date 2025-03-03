import os
import subprocess

# Ensure psutil is installed
try:
    import psutil
except ImportError:
    print("psutil not found, installing...")
    subprocess.run(["pip3", "install", "--user", "psutil"], check=True)
    import psutil  # Try importing again

def get_system_info():
    print("System Information:")
    print("-------------------")
    print(f"Hostname: {os.uname().nodename}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
    get_system_info()
