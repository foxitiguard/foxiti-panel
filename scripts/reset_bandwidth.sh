#!/bin/bash

# foxitiPanel Bandwidth Reset Script
# This script resets bandwidth usage for all domains in foxitiPanel

echo "foxitiPanel Bandwidth Reset Script"
echo "================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (use sudo)"
    exit 1
fi

# Check if foxitiPanel is installed
if [ ! -f "/usr/local/FoxitiCP/bin/python" ]; then
    echo "foxitiPanel not found. Please ensure foxitiPanel is installed."
    exit 1
fi

echo "Resetting bandwidth for all domains..."
echo ""

# Run the bandwidth reset script
/usr/local/FoxitiCP/bin/python /usr/local/FoxitiCP/plogical/bandwidthReset.py --reset-all

if [ $? -eq 0 ]; then
    echo ""
    echo "Bandwidth reset completed successfully!"
    echo ""
    echo "To verify the reset, you can:"
    echo "1. Check the foxitiPanel logs: /usr/local/lscp/logs/error.log"
    echo "2. Check individual domain bandwidth in foxitiPanel web interface"
    echo "3. Check bandwidth metadata files: ls -la /home/foxitipanel/*.bwmeta"
else
    echo ""
    echo "Bandwidth reset failed. Please check the logs for details."
    echo "Log file: /usr/local/lscp/logs/error.log"
    exit 1
fi

echo ""
echo "Note: This script only resets the displayed bandwidth values."
echo "The actual bandwidth calculation will resume from the current access logs."
echo "For a complete reset, you may also need to clear access logs if desired."
