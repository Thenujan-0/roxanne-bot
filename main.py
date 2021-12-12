#!/usr/bin/env python3




from telegram.ext import *


import responses as res

import os
import logging
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from sqlalchemy import create_engine , Integer,String,Column ,ForeignKey,BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker ,relationship

    
import datetime
from datetime import timedelta


#import dateutil.tz
import telegram
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from zoneinfo import ZoneInfo

from datetime import datetime as dt
from datetime import timedelta 
import threading


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

    logger = logging.getLogger(__name__)

bff= '-1001205686057'
temp = '-563465499'


waiting_for_response = None
def chrome_driver():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument(
    #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    pass
if __name__=='__main__':
    # chrome_driver()
    pass

elif  __name__ == 'main':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    # driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)




PORT = int(os.environ.get('PORT',5000))
API_KEY = os.environ.get('API_KEY_ROXANNE')


bot = telegram.Bot(API_KEY)

def start(update,context):
    update.message.reply_text('say something')

def help(update,context):
    update.messsage.reply_text('im not in the mood to help you')

def get_chat_id(update, context):
    chat_id = -1

    if update.message is not None:
       # from a text message
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        # from a callback message
        chat_id = update.callback_query.message.chat.id
        send_text = 'https://api.telegram.org/bot' + API_KEY + '/sendMessage?chat_id=' + bff + '&parse_mode=Markdown&text=' + chat_id

    # update.message.reply_text(chat_id)
    # update.message.reply_text(str(update.message.from_user.id))
    return chat_id

def get_user_id(update, context):
    user_id = -1
    if update.message is not None:
        user_id = update.message.from_user.id
    return user_id


def bittu(update,context):
    msg = str(update.message.text)
    chat_id =get_chat_id(update,context)
    if chat_id == int(bff):
        update.message.reply_text(' bittu is not allowded in this group')
    else:

        num = 5
        final_word = ''
        words = msg.split(' ')
        searches = []
        bittu_tag =words.index('/bittu')
        # print('index of bittu is'+str(bittu_tag))
        if bittu_tag >-1 and not words[-1].isdigit():
            for i in range(bittu_tag+1,len(words)):
                if final_word == '':
                    final_word+=words[i]

                else:
                    final_word+= '+'
                    final_word+= words[i]
        if bittu_tag >-1 and  words[-1].isdigit():
            for i in range(bittu_tag+1,len(words)-1):
                if final_word == '':
                    final_word+=words[i]

                else:
                    final_word+= '+'
                    final_word+= words[i]

        try:
            if words[len(words)-1].isdigit():
                num = int(words[len(words)-1])
                print(words[bittu_tag+1])
        except Exception :
            pass
        
        html_text = requests.get(f'https://www.pornpics.com/?q={final_word}').text 
        soup = BeautifulSoup(html_text,'lxml')
        
        # print(soup.prettify)
        images = soup.find_all('img')
        print('')
        
        # print(images)
        # print(soup.find('ofgYyuKcboI0LM'))
        for img in images:

            if img['src'][0] != '/':

                try:
                    searches.append(img['data-src'])
                except Exception:
                    print('no data src')
        # print(searches)
        variab = 0

        for search in searches:
            
            if variab < num:
                # print(search)
            
                payload ={
            'chat_id':chat_id,
                'photo': search,
                }
                variab += 1
                to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(API_KEY)
                resp = requests.post(to_url,data=payload)
                # print(resp.text)

def find_fac(num):
    var = num
    fac =1
    while var >0:
        
        fac *=var
        var-=1
    return fac


def fac(update,context):
    msg = str(update.message.text)
    words = msg.split(' ')
    
    if len(words)==1 :
        update.message.reply_text('wrong format')
    words.pop(0)
    
    not_word_err=False
    for word in words:
        if not word.isdigit():
            not_word_err= True

    if not_word_err:
        update.message.reply_text('looks like not all arguments are numbers')
    
    else:
        to_snd = ' '
        chat_id = get_chat_id(update,context)
        grtr= False
        for word in words:
            if int(word)<31:
                to_snd = to_snd + str(find_fac(int(word))) + "\n"
            else:
                grtr= True
        if to_snd!=' ':
            update.message.reply_text(to_snd)
        if grtr:
        
            update.message.reply_text('i wont tell you the factorial for numbers greater than 30')
            payload ={
            'chat_id':chat_id,
                'photo': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/59509a0c-9f3a-4b93-879a-839598904189/d5wvia8-e752a93b-2b7a-4b10-a99e-da3e3fde4373.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi81OTUwOWEwYy05ZjNhLTRiOTMtODc5YS04Mzk1OTg5MDQxODkvZDV3dmlhOC1lNzUyYTkzYi0yYjdhLTRiMTAtYTk5ZS1kYTNlM2ZkZTQzNzMuanBnIn1dXX0.ScWQTqDVU7UfEK75Y3HXO2gAte4FuF-5qry3zlkxBSY',
                }

            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(API_KEY)
            resp = requests.post(to_url,data=payload)
            # print(resp.text)
   
        
def range_fac(n1,n2):
    var = n1
    fac =1
    while var >n2:
        
        fac *=var
        var-=1
    return fac

if __name__ == '__main__':
    def tellThenujan():
        bot.send_message('1185281888','Bot started from heroku 😎')
    

def find_ncr(n,r):
    if n/2 >r:
        if r <100:
            calc =range_fac(n,n-r)
            bottom1 = find_fac(r)
        else:
            return 'too big'
    if n/2 <=r:
        if n-r<100:
            calc =range_fac(n,r)
            bottom1 = find_fac(n-r)
        else:
            return 'too big'
    if n <r :
        return 'thats not possible'



    answer = calc / bottom1
    return str(answer)
    
def find_npr(n,r):
    if n>r and r <300:
        return range_fac(n,n-r)
    else:
        return 'too big'

def ncr(update,context):
    message = str(update.message.text).lower()
    words = message.split(' ')
    if words[1].isdigit() and words[2].isdigit():
        update.message.reply_text(find_ncr(int(words[1]),int(words[2])))

def npr(update,context):
    message = str(update.message.text).lower()
    words = message.split(' ')
    if words[1].isdigit() and words[2].isdigit():
        update.message.reply_text(find_npr(int(words[1]),int(words[2])))
        
        
dictionary ={'waiting_for_response':None,'time':''}

#? lets talk about the reminders
# reminder works by a set of functions that are called when a response is received
# user will first call the reminder function it will ask for the title and update the database 
# database stores information about the user's answer i mean database is what tells the program which question the user is answering right now
# Data table is used for this purpose
# only the records with the name 'waiting_for_response' is used for this purpose
# data1 of these records is user_id 
# data2 of these records is chat_id
# and the data3 is the name of the function that is called when a response is received
# the function in the data3 will be called with the response (update,context)






def reminder(update,context):
    update.message.reply_text('Send me the title of the reminder.')
    
    chat_id = str(get_chat_id(update,context))
    
    
    user_id = str(get_user_id(update,context))
    # print('suer_id:',user_id)
    # print('chat id ',chat_id)
    data =session.query(Data).filter(Data.name=='waiting_for_response'+user_id+chat_id \
        ,Data.data1==user_id,Data.data2==chat_id).first()
    
    if data:
        data.data3='title'
    else:
        print('record not found so adding ----------------------------')
        session.add(Data('waiting_for_response'+user_id+chat_id,user_id,chat_id,'title'))

    session.commit()
reminders = []

def title(update,context):
    title =str(update.message.text)
    chat_id=str(get_chat_id(update,context))
    user_id = str(get_user_id(update,context))
    rows = session.query(Reminder)

    temp = 0
    nums_in_table=[]
    for row in rows:
        nums_in_table.append(row.id)
        if row.id >temp :
            temp= row.id
            
    final =-1
    for num in range(temp+1):
        if num not in nums_in_table:
            final = num
    
    if final ==-1:
        final=temp+1
        
    if len(title)<50:
        session.add(Reminder(final,title,chat_id=int(chat_id),user_id=int(user_id),))
        session.commit()
        dictionary['waiting_for_response']=time_ 
        update.message.reply_text('enter the time in 24 hours like shown below')
        update.message.reply_text('14:20')
        # time_()
        data =session.query(Data).filter(Data.name=='waiting_for_response'+user_id+chat_id \
            ,Data.data1==user_id,Data.data2==chat_id).first()
        
        if data:
            data.data3='time_'
        else:
            session.add(Data('waiting_for_response'+user_id+chat_id,user_id,chat_id,'time_'))
        
        session.commit()
    else:
        update.message.reply_text("title too long it can't have more than 50 characters")
#in Data table ther will be records of Reminder times

#name = user_id
    
#data1 = chat_id    



def time_(update,context):
    time =str(update.message.text)
    
    try:
        #check if time string is valid
        conditions = len(time)==5 and time[0:2].isdigit() and \
            time[3:5].isdigit() and time[2]==':'
            
        
        # print(time[0:2],time[3:5],time[2])
        if conditions:
            
            hour= int(time[0:2])
            min= int(time[3:5])
            condition =conditions and hour<25 and min<61
            if condition:
                user_id = get_user_id(update,context)
                chat_id = get_chat_id(update,context)
                
                chat_id =str(chat_id)
                user_id = str(user_id)

                #Goes to data table to store time
                record = session.query(Data).filter(Data.name == user_id+chat_id,Data.data1 == chat_id).first()
                if record is  None:
                    
                    session.add(Data(user_id+chat_id,chat_id,time,''))
                    session.commit()
                    date(update,context)
                else:
                    record.data2 = time
                    # dictionary['waiting_for_response']=date
                    date(update,context)
            else:
                update.message.reply_text('invalid format please enter the time like show above')

        else:
            update.message.reply_text('invalid format please enter the time like show above')

    except:
        update.message.reply_text('invalid format please enter the time like show above')

    

def date(update,context):
    user_id =get_user_id(update,context)
    chat_id = get_chat_id(update,context)
    
    
    keyboard = [
                [InlineKeyboardButton("Today", callback_data='Today')],
                [InlineKeyboardButton("Tomorrow", callback_data='Tomorrow')],
                [InlineKeyboardButton("Custom", callback_data='Custom')]
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = 'Select the date'
    resp = update.message.reply_text(message_reply_text, reply_markup=reply_markup)
    message_id = resp.message_id
    print('message_id',message_id)
    session.add(Data('inlinekeyboard_msgid_chatid'+str(message_id)+str(chat_id),str(user_id)))
    session.commit()
    print(f'messageid{message_id} has been added to database with userid {user_id}')
    
    
# i have decided to store all the time in asia/colombo timezone 
# for Reminder database
    

#function that starts the thread to deliver reminder
def sender(id,):

    record=session.query(Reminder).filter(Reminder.id == id).first()
    time_now =dt.now(ZoneInfo('Asia/Colombo'))
    # print('time now is --------------------------------------------------------| '+str(time_now))
    
    time_now = time_now.replace(tzinfo=None)
    # print(time_now)
    time_exec=record.time 
    # print(time_exec)
    # print('time_exec',len(time_exec))
    time_exec =dt.strptime(time_exec,'%Y-%m-%d %H:%M:%S.%f')
    # print(time_exec)
    time_dif =time_exec-time_now
    if time_dif.total_seconds()>0:
        print('a single thread is gonnna sleep for',time_dif.total_seconds(),'seconds')
        time.sleep(time_dif.total_seconds())
        
        chat_id=record.chat_id
        title = record.title
        bot.send_message(chat_id,title)
        if record.repeat=='':
            
            keyboard = [
                        [InlineKeyboardButton("Yes", callback_data='reshedule')],
                        [InlineKeyboardButton("No", callback_data='no_reshedule')],
                    ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            # print('inlinekeyboard_msgid_chatid'+str(message_id)+str(chat_id),str(user_id))
            
            # to_be_deleted=session.query(Data).filter(Data.name=='inlinekeyboard_msgid_chatid'+str(message_id)+str(chat_id)).first()
            # session.delete(to_be_deleted)
            message_reply_text = 'Do you want to reshedule this reminder '
            resp =bot.send_message(text=message_reply_text,chat_id=chat_id,reply_markup=reply_markup)
            session.delete(record)
        else:
            reminder_time=record.time
            reminder_time=dt.strptime(reminder_time,'%Y-%m-%d %H:%M:%S.%f')
            reminder_time=reminder_time+timedelta(days=7)
            record.time =str(reminder_time)
        session.commit()
    else:
        bot.send_message(text='Sorry man i cant time travel because im afraid i might change the present ',chat_id=record.chat_id)
        session.delete(record)
        session.commit()




        

def start_all_reminders():
    reminders = session.query(Reminder)
    array1 = []
    for reminder in reminders:
        if len(reminder.time)==26:

            reminder_time=dt.strptime(reminder.time,'%Y-%m-%d %H:%M:%S.%f')
            time_now= dt.now(ZoneInfo('Asia/Colombo'))
            time_now= time_now.replace(tzinfo=None)
            print(reminder.title)
            print((reminder_time-time_now).total_seconds())
            if (reminder_time-time_now).total_seconds() > 0:
                array1.append(threading.Thread(target=sender,args=[reminder.id]))
            else:
                if reminder.repeat=='':
                    session.delete(reminder)
                    session.commit()
                elif reminder.repeat=='everyweek':
                    reminder_time=reminder.time
                    reminder_time=dt.strptime(reminder_time,'%Y-%m-%d %H:%M:%S.%f')
                    reminder_time=reminder_time+timedelta(days=7)
                    reminder.time =str(reminder_time)+'.000000'
                    session.commit()
                    array1.append(threading.Thread(target=sender,args=[reminder.id]))
                    
        elif len(reminder.time)!='':
            session.delete(reminder)
            session.commit()
    print('reminders that are gonna get started:',array1)
    if len(array1) > 0:
        for elem in array1:
            elem.start()
            


array=[]



def cancel(update,context):
    user_id =str(get_user_id(update,context))
    chat_id=str(get_chat_id(update,context))
    record =session.query(Data).filter(Data.name=='waiting_for_response'+user_id+chat_id).first()
    record.data3=''
    session.commit()
       
def press_button_callback( update,context):

    
    
    
    msg =str(update.callback_query.data)
    user_id=str(update.callback_query.from_user.id)
    chat_id=str(update.callback_query.message.chat.id)
    record_function =session.query(Data).filter(Data.name=='waiting_for_response'+user_id+chat_id,\
        Data.data1==user_id,Data.data2==chat_id).first() 
    
    
    message_id =update.callback_query.message.message_id
    print('checking for message_id:',message_id)
    record =session.query(Data).filter(Data.name=='inlinekeyboard_msgid_chatid'+str(message_id)+str(chat_id)).first()
    required_user_id = record.data1
    
    if required_user_id==user_id:
    
        bot.delete_message(chat_id,message_id,timeout=None)
        if msg=='Today' or msg=='Tomorrow':
            bot.send_message(text=f'reminder set for{msg}',chat_id=chat_id)
            # recieving the reminder time from the database
            
        
            time = session.query(Data).filter(Data.name==user_id+chat_id,Data.data1==chat_id).first().data2
            date = datetime.datetime.now(ZoneInfo('Asia/Colombo')).date()
            if msg=='Tomorrow':
                date=date+timedelta(days=1)
            # print(time)
            # print(date)
            datetime_str=str(date)+' '+time+':00.000000'
            # print(datetime_str)
            time1=datetime.datetime.strptime(datetime_str,'%Y-%m-%d %H:%M:%S.%f')
            # utc_time = time1.replace(tzinfo=dateutil.tz.gettz('Asia/Colombo')).astimezone(pytz.utc)
            # utc_time = utc_time.replace(tzinfo=None)
            # print(utc_time)
            records =session.query(Reminder).filter(Reminder.user_id==user_id,Reminder.chat_id==chat_id)
            for record in records:
                if record.time=='':
                    print('found the record to add datetime')
                    record.time =datetime_str
                    session.commit()
                    array.append(threading.Thread(target=sender,args=[record.id]))
                        
            array[-1].start()
            print(array[-1],'the thread that is getting started ')
            record_function.data3=''
            session.commit()
                
                
                
        elif msg=='Custom':
            bot.send_message(text=f'Enter the date like shown below or just copy and send back after editing',chat_id=chat_id)
            bot.send_message(text=str(datetime.datetime.now().date()),chat_id=chat_id)
            
        

            record_function.data3='custom_date'
            session.commit()
        
        if msg in ('Today','Tomorrow','Custom'):
            keyboard = [
                        [InlineKeyboardButton("Yes", callback_data='repeat')],
                        [InlineKeyboardButton("No", callback_data='no_repeat')],
                    ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            print('inlinekeyboard_msgid_chatid'+str(message_id)+str(chat_id),str(user_id))
            
            to_be_deleted=session.query(Data).filter(Data.name=='inlinekeyboard_msgid_chatid'+str(message_id)+str(chat_id)).first()
            session.delete(to_be_deleted)
            message_reply_text = 'Do you want to repeat this reminder every week'
            resp =bot.send_message(text=message_reply_text,chat_id=chat_id,reply_markup=reply_markup)
            session.add(Data('inlinekeyboard_msgid_chatid'+str(resp.message_id)+str(chat_id),str(user_id)))
            session.commit()
        
        if msg=='repeat':
            records =session.query(Reminder).filter(Reminder.user_id==user_id,Reminder.chat_id==chat_id)
            for record in records:
                if record.repeat=='':
                    print('found the record to add repeat')
                    record.repeat ='everyweek'
                    session.commit()

    else:
        bot.send_message(text='You are not supposed to press the button idiot'+str(update.callback_query.message.chat.username),chat_id=chat_id)
        bot.send_photo(chat_id=chat_id,photo='https://i.pinimg.com/originals/22/05/ef/2205ef2dae42143507342d783b140dc1.jpg',caption='Fuck you')


def delete_reminder(update,context):
    msg =str(update.message.text)
    words =msg.split(' ') 
    words.pop(0)
    if len(words) ==0:
        update.message.reply_text('enter the number of the reminder you want to delete')
    
    else:
        for num in words:
            num =int(num)
            record = session.query(Reminder).filter(Reminder.id==num).first()
            session.delete(record)
        session.commit()

   
def my_reminders(update,context):
    chat_id=str(get_chat_id(update,context))
    user_id=str(get_user_id(update,context))
    records =session.query(Reminder).filter(Reminder.user_id==user_id,Reminder.chat_id==chat_id)
    string=''

    for record in records:
        string = string+ str(record.id)+' '+record.title+'\n'+record.time[0:17]+'\n'
    if len(string)<2:
        update.message.reply_text('no reminders found')
    else:
        string="```\n"+string+"\n```"
        update.message.reply_text(string,parse_mode="Markdown")
    
    
def custom_date(update,context):
    msg = str(update.message.text)
    user_id=str(get_user_id(update,context))
    chat_id= str(get_chat_id(update,context))
    try:
        condition = len(msg)==10 and msg[0:4].isdigit() and msg[5:7].isdigit() \
            and msg[8:10].isdigit() and msg[4]=='-' and msg[7]=='-' 
    except:
        condition = False
    if condition:
        update.message.reply_text('custom date set succesfully')
        record =session.query(Data).filter(Data.name ==user_id+chat_id).first()
        time =record.data2
        
        date=msg   
        datetime_str=str(date)+' '+time+':00.000000'
        time1=datetime.datetime.strptime(datetime_str,'%Y-%m-%d %H:%M:%S.%f')

        session.commit()
        record =session.query(Reminder).filter(Reminder.user_id==user_id,Reminder.chat_id==chat_id,Reminder.time=='').first()
        
        if record.time=='':
            print('found the record to add datetime')
            record.time =datetime_str
            session.commit()
            array.append(threading.Thread(target=sender,args=[record.id]))
                    
        array[-1].start()
        
        record_function =session.query(Data).filter(Data.name=='waiting_for_response'+user_id+chat_id).first()
        # changing the waiting_for_response to None
        record_function.data3=''
        session.commit()
        
    else:
        update.message.reply_text('custom date was sent in wrong format')
    
    
def handle_message(update,context):
    message = str(update.message.text).lower()
    msgid = update.message.message_id
    chat_id = get_chat_id(update,context)
    print(msgid,chat_id)
    # resp = bot.delete_message(chat_id, message_id =msgid,timeout =None)
    # print(resp)
    user_id = get_user_id(update,context)
    # print(message)
    resp = res.respond(message,chat_id)
    # print(resp,'response')
    # print(chat_id)
    
    waiter =session.query(Data).filter(Data.name=='waiting_for_response'+str(user_id)+str(chat_id), \
        Data.data1==str(user_id),Data.data2==str(chat_id)).first()
    # print('theone',waiter.data3)
    if waiter:
        if waiter.data3 !='':

            print(f'executing {waiter} with arguments')
            eval(waiter.data3+'(update,context)')
            
        if waiter.data3=='' and resp is not None:
            update.message.reply_text(resp)
    if not waiter and resp is not None:
        update.message.reply_text(resp)

def error(update,context):  
    try:
        logger.warning('Update "%s" caused error "%s"', update, context.error)
    except Exception as e:
        print(str(e))
        logging.debug('Update "%s" caused error "%s"', update, context.error)



            



def my_id(update,message):
    user = update.message.from_user
    update.message.reply_text('user id is {}'.format(user['id']))


Base = declarative_base()


class Reminder(Base):
    __tablename__='reminder'
    id=Column('id',Integer, primary_key=True)
    title = Column('title',String(50))
    time = Column('time',String(30),)
    description = Column('description',String(100))
    chat_id = Column('chat_id',BigInteger,nullable=False)
    user_id = Column('user_id',Integer,nullable=False)
    repeat =Column('repeat',String,nullable=True)

    
    
    def __init__(self,id,title,chat_id,user_id,time='',description='',repeat=''):

        self.id = id
        self.title = title
        self.time = time
        self.description = description
        self.chat_id = chat_id
        self.user_id = user_id
        self.repeat=repeat
        




class Data(Base):
    __tablename__ = 'data'
    name= Column('name',String(50),unique=True,nullable=False,primary_key=True)
    data1= Column('data1',String)
    data2= Column('data2',String)
    data3= Column('data3',String)


    def __init__(self,name,data1='',data2='',data3=''):
        self.name =name
        self.data1= data1
        self.data2=data2
        self.data3= data3


engine = create_engine('postgresql+psycopg2://qrlqxjwb:z1qf3iQw0tz5KVgg9w-lHFN19MiX-4G5@batyr.db.elephantsql.com/qrlqxjwb',echo=False)

Base.metadata.create_all(bind=engine)
Session= sessionmaker(bind=engine)
session= Session()

pava=1077764018
thenu=1185281888




start_all_reminders()

tellThenujan()



updater = Updater(API_KEY,use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('help',help))
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('reminder',reminder))
dp.add_handler(CommandHandler('cancel',cancel))
dp.add_handler(CommandHandler('my_reminders',my_reminders))
dp.add_handler(CommandHandler('delete_reminder',delete_reminder))


dp.add_handler(CallbackQueryHandler(press_button_callback))
dp.add_handler(MessageHandler(Filters.text,handle_message))

dp.add_error_handler(error)

if __name__ == '__main__':
    updater.start_webhook(listen='0.0.0.0',port=int(PORT),url_path=API_KEY)
    updater.bot.setWebhook('https://roxanne-bot.herokuapp.com/' + API_KEY)
    updater.idle()

