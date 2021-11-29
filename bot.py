import telebot

bot = telebot.TeleBot("2136415609:AAEiMtmvGKhbvgm-GBdeeqTdA5S8Mbyc1oY")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, message.text)


bot.polling( none_stop= True )


