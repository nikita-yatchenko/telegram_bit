import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello_message(message):
    reply = f"Hello {message.from_user.first_name}, this bot makes it easy to navigate group chats"
    bot.send_message(message.chat.id, reply)


@bot.inline_handler(func=lambda query: True)
def query_text(message):
    print(message)
    bot.send_message(message.chat.id, message, parse_mode='html')


@bot.message_handler(content_types=['text'])
def query_text(message):
    print(message)
    bot.send_message(message.chat.id, message, parse_mode='html')

# start bot
bot.polling(none_stop=True)
