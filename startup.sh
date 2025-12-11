#!/bin/bash
cd /home/pi/smart_reader
source venv/bin/activate
# optional: export DISPLAY if you need GUI
python main.py >> smartreader.log 2>&1
