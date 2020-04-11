
# -*- coding: utf-8 -*- 
import config 
import telebot 
tb = telebot.Telebot(config.token)
@tb.message_handler(commands=['ke'])
def answer(message):
    tb.send_message(message.chat.id, "хочу сигуууууу")

tb.polling(none_stop=False, interval = 0, timeout = 20)



