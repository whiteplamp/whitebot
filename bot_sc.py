import config
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, i'm bot, my developer is Alexandra Netskaya, I can do only one thing. And it is write message.")
    bot.send_message(message.chat.id, 'Choose action')
    
    markup = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('1')
    b = types.KeyboardButton('2')
    c = types.KeyboardButton('3')
    d = types.KeyboardButton('/back')
    markup.row(a,b)
    markup.row(c)
    markup.row(d)
    bot.send_message(message.chat.id, "Choose letter:", reply_markup = markup)
    @bot.message_handler(content_types=['text'])
    def test_message(message):
        if message.text == '1':
            bot.send_message(message.chat.id, '1')
        elif message.text == '2':
            bot.send_message(message.chat_id, '1')
        bot.send_message(message.chat.id, '/start')
       

bot.polling(none_stop=False, interval = 0, timeout = 20)
