# importing all required libraries
import telebot
import os


def enviar_mensaje(message):

    # get your api_id, api_hash, token
    # from telegram as described above
    #api_id = os.environ.get('api_id')
    #api_hash = os.environ.get('api_hash')
    token = os.environ.get('token')
    user_telegram = os.environ.get('user_telegram')

    api_id = '17143890'
    api_hash = '45143b37aa797e9dc15a0c7fdd027bbe'
    token = '5202593674:AAFbeOu2OcuQ0Edjpe-Aq2UMuknLPD0Pp-I'

    # Create bot
    bot = telebot.TeleBot(token)

    # Send message
    bot.send_message(user_telegram, message)

