#!/bin/bash

echo "Script to install Apache" > /tmp/silly.txt

sudo yum update -y
sudo yum install -y httpd
sudo systemctl restart httpd.service
