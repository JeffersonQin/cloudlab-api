#!/bin/bash

sudo apt-get update && sudo apt-get install -y python3-pip
cd /local/repository || exit
pip3 install -r requirements.txt
