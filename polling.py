#!/usr/bin/env python3
from time import sleep
import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify
Notify.init('roxanne')

def notifier(msg):
    temp_noti=Notify.Notification.new(msg)
    temp_noti.set_urgency(1)
    temp_noti.show()


notifier('started roxanne')

# sleep(45)
notifier('started runnning roxanne')
sleep(1)
# from telegram.ext import *

sleep(1)
from main import *


import multiprocessing
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import subprocess
import logging

sleep(10)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='/home/thenujan/roxanne.log',
                    level=logging.DEBUG,)


logging.info('started')



out=subprocess.check_output(['heroku maintenance:on -a roxanne-bot'],shell=True).decode()

logging.debug(out)

    # random_number = str(random())
    # keyboard = [heroku maintenance:on -a roxanne-bot
    #             [InlineKeyboardButton('You lost' , callback_data='callback_1')],
    #             [InlineKeyboardButton('Click button 1 ' + random_number, callback_data='callback_2')]
    #         ]

    # reply_markup = InlineKeyboardMarkup(keyboard)
    # update.callback_query.edit_message_reply_markup(reply_markup)
bot.send_message('1185281888','Bot started')
print(dt.now(ZoneInfo('Asia/Colombo')))



updater.start_polling()
updater.idle()




