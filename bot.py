import telebot

Token ="6691992182:AAEbF3OOq7fNEmRGeU6piHLQwMrQpaSc9RI"
bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to Bhaktione")
    bot.reply_to(message,"""What You Want to start With
                 1. Strotas
                 2. Panchang
                 3. Hinduism Stories""")


@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"""How Can i Help You 
                 """)


@bot.message_handler(['strotas'])
def help(message):
    bot.reply_to(message, "https://youtube.com/playlist?list=PLEK6TOzUNTb7mkwAqCtIZ0hAYoaxrg5vN&si=rl6Y-Bj68bwrUjdx")
@bot.message_handler(['panchang'])
def help(message):
    bot.reply_to(message, "https://youtube.com/playlist?list=PLEK6TOzUNTb6gru1GkNLQQiNEl-Y6o_pK&si=NnUs3gNkbHB2AcO6")

@bot.message_handler(['hinduism'])
def help(message):
    bot.reply_to(message, "https://youtube.com/playlist?list=PLEK6TOzUNTb6LOCawZLiAUJHfxpufGK9C&si=6sLw-URTEowcn0yR")


bot.polling()