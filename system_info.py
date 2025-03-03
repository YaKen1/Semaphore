print("System Information:")
print("-------------------")

# Get the hostname
hostname = open("/etc/hostname").read().strip()
print(f"Hostname: {hostname}")

# Get the OS information
os_info = open("/etc/os-release").read().split("\n")[0].replace('NAME=', '').replace('"', '')
print(f"OS: {os_info}")

# Get CPU information
cpu_info = open("/proc/cpuinfo").read().split("\n")[4].split(":")[1].strip()
print(f"CPU: {cpu_info}")

# Get total memory
for line in open("/proc/meminfo"):
    if "MemTotal" in line:
        mem_total = line.split(":")[1].strip()
        print(f"Memory: {mem_total}")
        break

# Get system uptime
uptime = open("/proc/uptime").read().split()[0]
uptime_hours = int(float(uptime) // 3600)
uptime_minutes = int((float(uptime) % 3600) // 60)
print(f"Uptime: {uptime_hours}h {uptime_minutes}m")
