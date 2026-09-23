#!/bin/bash
## Script to clear caches after static file changes. Useful for development and testing.
## All credit belongs to Usman Nasir
## To use make it executable
## chmod +x /usr/local/FoxitiCP/upgrade.sh
## Then run it like below.
## /usr/local/FoxitiCP/upgrade.sh

# Check if virtual environment exists
if [[ ! -f /usr/local/FoxitiCP/bin/python ]]; then
    echo "Error: foxitiPanel virtual environment not found at /usr/local/FoxitiCP/bin/python"
    echo "Please ensure foxitiPanel is properly installed."
    exit 1
fi

cd /usr/local/FoxitiCP && /usr/local/FoxitiCP/bin/python manage.py collectstatic --no-input
rm -rf /usr/local/FoxitiCP/public/static/*
cp -R  /usr/local/FoxitiCP/static/* /usr/local/FoxitiCP/public/static/
# CSF support removed - discontinued on August 31, 2025
# mkdir /usr/local/FoxitiCP/public/static/csf/
find /usr/local/FoxitiCP -type d -exec chmod 0755 {} \;
find /usr/local/FoxitiCP -type f -exec chmod 0644 {} \;
chmod -R 755 /usr/local/FoxitiCP/bin
chown -R root:root /usr/local/FoxitiCP
chown -R lscpd:lscpd /usr/local/FoxitiCP/public/phpmyadmin/tmp
systemctl restart lscpd
