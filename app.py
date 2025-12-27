# import telebot

# bot = telebot.TeleBot("7525871391:AAHep7vQLbitniFHiZLut13KdL338hyyyec")

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(
#         message.chat.id,
#         f"Merhaba {message.from_user.first_name} 👋\n\n"
#         "Komutlar:\n"
#         "- hello world\n"
#         "- id\n"
#         "- /help"
#     )

# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(
#         message.chat.id,
#         "<b>Help</b>\n"
#         "<em>hello world</em> → selam verir\n"
#         "<em>id</em> → kullanıcı ID gösterir",
#         parse_mode="HTML"
#     )

# @bot.message_handler(func=lambda message: True)
# def info(message):
#     if message.text.lower() == "hello world":
#         bot.send_message(
#             message.chat.id,
#             f"Hello, ( {message.from_user.first_name}"
#         )

#     elif message.text.lower() == "id":
#         bot.send_message(
#             message.chat.id,
#             f"ID: {message.from_user.id}"
#         )

# bot.polling(none_stop=True)

# import telebot


# bot = telebot.TeleBot("7525871391:AAGoEM2iRCKtv8T21YhpRj6swZGyxdeKtrU")


# @bot.message_handler(commands=['start', "main"])
# def main(message):
#     bot.send_message(message.chat.id)

# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode="html")

# bot.polling(none_stop=True)
import telebot
import webbrowser
from telebot import types

# Not: Token'ını paylaştığın için başkaları botunu kontrol edebilir. 
# Gerçek projelerde token'ı gizli tutmalısın.
bot = telebot.TeleBot("7525871391:AAHl3VEwNvTtmA5A2KaU3JCI05xlf5Oy8yQ")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Visit Website", url="https://gemini.google.com")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Delete photo", callback_data="delete")
    btn3 =types.InlineKeyboardButton("Edit photo", callback_data="edit")
    markup.row(btn2 , btn3)
    bot.reply_to(message, "Nice photo!" , reply_markup=markup)

@bot.message_handler(commands=['site', 'website'])
def site(message):webbrowser.open("https://gemini.google.com/app/")


# 1. ÖNCE KOMUTLAR (Start, Help vb.)
@bot.message_handler(commands=['start', 'main'])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name} {message.from_user.last_name}")

@bot.message_handler(commands=['help'])
def help_command(message): # Fonksiyon isimleri farklı olmalı
    bot.send_message(
        message.chat.id,
        '<b>Help</b> <em><u>information</u></em>',
        parse_mode="html"
    )

# 2. EN SON GENEL MESAJLAR
@bot.message_handler()
def info(message):
    if message.text.lower() == "hello world":
        bot.send_message(
            message.chat.id,
            f"Hello, {message.from_user.first_name} {message.from_user.last_name}"
        )
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")

bot.polling(none_stop=True)