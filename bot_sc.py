import config
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, i'm bot, my developer is Alexandra Netskaya, I can do only one thing. And it is write message.")
    bot.send_message(message.chat.id, 'Choose action')
    markup = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('echo')
    b = types.KeyboardButton('hey')
    markup.row(a)
    markup.row(b)
    bot.send_message(message.chat.id, "Choose letter:")


bot.polling(none_stop=False, interval = 0, timeout = 20)
