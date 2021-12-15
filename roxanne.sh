#! /bin/sh
sleep 1

heroku maintenance:on -a roxanne-bot

python3 /home/thenujan/Desktop/Code/Roxanne/polling.py
