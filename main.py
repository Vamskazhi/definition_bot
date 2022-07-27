import re
import os
from config import settings
from telebot import TeleBot
from wikipedia import set_lang, page


def get_token():
    try:
        token = settings.token
    except AttributeError as er:
        token = os.getenv('TOKEN')
    return token


bot = TeleBot(get_token())
set_lang("ru")


def get_wiki(s):
    try:
        ny = page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki(message.text))


bot.polling(none_stop=True, interval=0)
