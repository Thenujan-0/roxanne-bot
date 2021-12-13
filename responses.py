import requests
import random
from bs4 import BeautifulSoup
import os
import telegram
API_KEY = os.environ.get('API_KEY_ROXANNE')







bot = telegram.Bot(API_KEY)
bff= '-1001205686057'
temp = '-563465499'



fuck =('fuck','fuck you','fuck yourself','fuck off','🖕')

love = ('love you','i love you','i love you too','love you  too','love you so much','i love you more')

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
        if int(chat_id) >0:
            return random.choice(unknown)
    return find_reply(input_text,chat_id)
