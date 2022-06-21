#!/bin/bash

sudo apt-get python3-pip
pip install --upgrade pip

pip install flask
pip install requests
pip install bs4
pip install selenium
pip install webdriver-manager

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

sudo wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

cd OSP_Team

chmod +x app.py
python3 app.py
