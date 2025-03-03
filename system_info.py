import os
import psutil

def get_system_info():
    print("System Information:")
    print("-------------------")
    print(f"Hostname: {os.uname().nodename}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
    get_system_info()
