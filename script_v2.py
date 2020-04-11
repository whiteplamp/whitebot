
# -*- coding: utf-8 -*- 
import config 
import telebot 
bot = telebot.TeleBot(config.token) 
@bot.message_handler(commands=["test"]) 
def send_hello(message): # Название функции не играет никакой роли, в принципе 
    bot.send_message(message.chat_id, "Хочу сижжжжжку?") 
bot.polling()
