
import random

import telebot
from telebot.types import Message


TOKEN = '869034643:AAFbs_FG-jxJoXyeNm2b4XzvnsDB6C76Jsk'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types = ['text'])
@bot.edited_message_handler(content_types = ['text'])
def echo_digits(message):
	if '/start' in message.text:
		bot.reply_to(message, 'Привет, меня создал Влад :) \nНапиши свое имя')
		return
	if "Настя" in message.text:
		bot.reply_to(message, 'Влад говорит, что Настя лучше всех')
		return
	if "настя" in message.text:
		bot.reply_to(message, 'Влад говорит, что Настя лучше всех')
		return
	if "Настюшка" in message.text:
		bot.reply_to(message, 'Влад говорит, что Настя лучше всех')
		return
	if "настюшка" in message.text:
		bot.reply_to(message, 'Влад говорит, что Настя лучше всех')
		return
	if 'саша'in message.text:
		bot.reply_to(message, 'Влад говорит, что Черный дилер - честный дилер')
		return
	if 'Саша'in message.text:
		bot.reply_to(message, 'Влад говорит, что Черный дилер - честный дилер')
		return
	if 'Саша Барышев'in message.text:
		bot.reply_to(message, 'Влад говорит, что Черный дилер - честный дилер')
		return
	if 'саша барышев'in message.text:
		bot.reply_to(message, 'Влад говорит, что Черный дилер - честный дилер')
		return
	if 'Влад'in message.text:
		bot.reply_to(message, 'Сытник лучше всех')
		return
	if 'Кирилл'in message.text:
		bot.reply_to(message, 'Влад говорит, что Кирилл любит мужские письки')
		return
	if 'кирилл'in message.text:
		bot.reply_to(message, 'Влад говорит, что Кирилл любит мужские письки')
		return
	if 'Кирич'in message.text:
		bot.reply_to(message, 'Влад говорит, что Кирилл любит мужские письки')
		return
	if 'кирич'in message.text:
		bot.reply_to(message, 'Влад говорит, что Кирилл любит мужские письки')
		return
	if 'Кирилл Байдуков'in message.text:
		bot.reply_to(message, 'Влад говорит, что Кирилл любит мужские письки')
		return
	if 'кирилл байдуков'in message.text:
		bot.reply_to(message, 'Влад говорит, что Кирилл любит мужские письки')
		return
	bot.reply_to(message, 'ошибка')
		 	
	




		

 
bot.polling(timeout = 60)



