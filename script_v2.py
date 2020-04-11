
# -*- coding: utf-8 -*- 
import config 
import telebot 
tb = telebot.TeleBot(config.token)
@tb.message_handler(commands=['start'])
def answer(message):
    tb.send_message(message.chat.id, "Hello, i'm test bot, which was made by Alexandra Netskaya")
    tb.send_message(message.chat.id, "I can repeat your messages, if you want it, you can write '/echo' for me")
@tb.message_handler(commands=['echo'])
def loop(message):
    tb.send_message(message.chat.id, "Your next message will be repeated by me, if you want to end repeating, just write '/exit'")
    @tb.message_handler(func = lambda message: message.text != "/exit")
    def echo(message):
        tb.send_message(message.chat.id, message.text)
    break
    

tb.polling(none_stop=False, interval = 0, timeout = 20)



