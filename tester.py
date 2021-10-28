
from telegram.ext import *
from main import *
import multiprocessing
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler






    # random_number = str(random())
    # keyboard = [
    #             [InlineKeyboardButton('You lost' , callback_data='callback_1')],
    #             [InlineKeyboardButton('Click button 1 ' + random_number, callback_data='callback_2')]
    #         ]

    # reply_markup = InlineKeyboardMarkup(keyboard)
    # update.callback_query.edit_message_reply_markup(reply_markup)
bot.send_message('1185281888','Bot started')
print(dt.now(ZoneInfo('Asia/Colombo')))


updater.start_polling()
updater.idle()




