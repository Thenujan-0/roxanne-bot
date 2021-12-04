#! /bin/sh
sleep 1
CURRENTDATE=`date +"%Y-%m-%d %T"`
echo "$API_KEY_ROXANNE is the environment var" >> /home/thenujan/temp.txt
echo "started $CURRENTDATE" >> /home/thenujan/Desktop/Code/Roxanne/logs/roxanne.log
heroku maintenance:on -a roxanne-bot

python3 /home/thenujan/Desktop/Code/Roxanne/polling.py
