#!/usr/bin/env python3
from time import sleep
import requests
import subprocess
import logging
subprocess.Popen(['pkill -f "python3 /home/thenujan/Desktop/Code/Roxanne/polling.py"'],shell=True)

subprocess.run(['heroku maintenance:off -a roxanne-bot'],shell=True)

requests.get('https://roxanne-bot.herokuapp.com')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='/home/roxanne.log')
logging.info('finished turning on cloud roxanne ')

