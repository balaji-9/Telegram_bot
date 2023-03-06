import telebot
from codechef import *

TOKEN = "5992588684:AAFZ-a2BkICJhC2O0CAOoKcg6-XczmVoyXE"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Welcome to Ratings Bot!\ntype /help to know commands")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"/codechef <Username> -> to know rating and no of problems solved")

@bot.message_handler(commands=['codechef'])
def ratings(message):
    text = message.text
    username = text[10:]
    if username == "":
        bot.reply_to(message, "Please Enter username")
        return
    info = codechef_ratings(username)
    if info == []:
        bot.reply_to(message, "Please Enter Valid username")
        return
    bot.reply_to(message, f"Name : {info[0]}\nRating : {info[1]}\nProblems_solved : {info[2]}")

print("Bot is running...")
bot.infinity_polling()
