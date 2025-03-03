#!/bin/bash

# Update system
echo "Updating system..."
sudo dnf update -y

# Install htop
echo "Installing htop..."
sudo dnf install -y htop

# Print system information
echo "System Information:"
echo "-------------------"
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime -p)"
echo "Memory Usage:"
free -h
echo "Disk Usage:"
df -h /
echo "CPU Load:"
uptime
