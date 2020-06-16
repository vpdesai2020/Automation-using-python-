from telegram.ext import Updater, CommandHandler
import requests
import re
from bs4 import BeautifulSoup

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, InlineQueryHandler)


def start(bot, update):
    source=requests.get('https://inshorts.com/en/read').text
    soup=BeautifulSoup(source,'lxml')
    for news in soup.find_all('div', class_='news-card-title news-right-box'):
        headings=news.span.text
        update.message.reply_text(headings)                            

def main():
    updater = Updater('KEY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
