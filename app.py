import telebot


bot = telebot.TeleBot("7525871391:AAGoEM2iRCKtv8T21YhpRj6swZGyxdeKtrU")


@bot.message_handler(commands=['start', "main"])
def main(message):
    bot.send_message(message.chat.id)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode="html")

bot.polling(none_stop=True)