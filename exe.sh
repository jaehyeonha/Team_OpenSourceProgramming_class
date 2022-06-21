#!/bin/bash

pip install re
pip install requests
pip install bs4
pip install time
pip install selenium
pip install webdriver-manager

google-chrome --version

sudo wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

cd
cd OSP_Team

chmod +x app.py
python3 app.py
