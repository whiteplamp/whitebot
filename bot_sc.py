import config
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, "Hello, i'm bot, my developer is Alexandra Netskaya, I can do only one thing. And it is write message.")
    bot.send_message(message.chat.id, 'Choose action')
markup = types.ReplyKeyboardMarkup
itembtna = types.KeyboardButton('echo')
itembtnb = types.KeyboardButton('hey')
markup.row(itembtna)
markup.row(itembtnb)
bot.send_message(chat_id, "Choose letter:", reply_markup = markup)


bot.polling(none_stop=False, interval = 0, timeout = 20)
