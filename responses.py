import requests
import random
from bs4 import BeautifulSoup
import os
import telegram
API_KEY = os.environ.get('API_KEY_ROXANNE')







bot = telegram.Bot(API_KEY)
bff= '-1001205686057'

names=('sunny','leone','@roxanne_telebot')

fuck =('fuck','fuck you','fuck yourself','fuck off','🖕')

love = ('love you','i love you','i love you too','love you  too','love you so much','i love you more')

hate=('i hate you','i hate you sunny','i hate you so much sunny')
hate_reply=('I though we had feelings for each other 🥀','😭','You are hurting my feelings 😭')
hi=('hi','hello','hey there','whatsup','hey','hii')

unknown = ('I wonder what that means 🤔',
           'I dont understand human language very well',
           'Can you please speak in binary so that i can understand',
           'Umm I\'m having a hard time understanding you ',
           'I only know few words in human language . 😅 Sorry',
           'It completely went over my head . Can you repeat the same in binary so that i can understand',
            )

def respond(input_text,chat_id):
    print('sending response')
    def find_reply(input_text,chat_id):
        msg= str(input_text).lower()
        print(msg)

        if msg in ('fuck','fuck you','fuck yourself','fuck off'):
            return random.choice(fuck)
        if msg in love : 
            print('yes man')
            bot.sendPhoto(photo='https://advicesacademy.com/wp-content/uploads/2015/10/Sunny-Leone-Kiss.jpg?_gl=1*1v74y7a*_ga*YW1wLUlGXzlHSF8xMm1GT2R4UE5VUjA1TkE.',chat_id=chat_id)
            
            return random.choice(love)
        
        if msg in hi: 
            return random.choice(hi)

        for sentence in hi:
            if msg.count(sentence)>0 and msg.count('sunny')>0:
                return random.choice(hi)
                
        
        if msg in ('what is your name','what\'s your name','what\'s your name?','whats your name?'):
            return 'the guy who made me forgot to give me a name'
                
        for sentence in love:
            if msg.count(sentence)>0 and msg.count('sunny')>0 :
                
                bot.sendPhoto(photo='https://advicesacademy.com/wp-content/uploads/2015/10/Sunny-Leone-Kiss.jpg?_gl=1*1v74y7a*_ga*YW1wLUlGXzlHSF8xMm1GT2R4UE5VUjA1TkE.',chat_id=chat_id)
                return random.choice(love)+ '❤️'+ '❤️'
            elif msg.count(sentence)>0 :
                return random.choice(love) + '❤️'
            
        text_in_binary = True
        called_me=False
        
        #check if it is binary input
        for i in range(len(input_text)):
            if not input_text[i] in ('1','0'):
                text_in_binary = False
                break
        
        
        #check if sunny was mentioned
        for i in range(len(names)):
            if names[i] in input_text:
                called_me=True
        
        if int(chat_id) >0 or called_me:
            if text_in_binary:
                return ('Thank you so much for the binary.But it just doesnt make much sense to me 🤔😥')
            
            if input_text in hate:
                return random.choice(hate_reply)
            if '@roxanne_telebot' ==input_text:
                return 'Yes sir \n or madam or whatever you are'
            return random.choice(unknown)
            
    return find_reply(input_text,chat_id)
