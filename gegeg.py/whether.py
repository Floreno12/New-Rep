import telebot
import requests
import json
from telebot import types

TOKEN = '6546548054:AAGpWFtLMD-y0yY5D6RNFAEa2-8uQe9jqUY'
bot = telebot.TeleBot(TOKEN)
api = '0582b1eeff342b13300d3ff4f0baef5d'


@bot.message_handler(commands=['погода'])
def get_start(message):
    bot.send_message(message.chat.id, 'Напишіть назву міста ')



@bot.message_handler(content_types=['text'])
def get_text(message):
    info_city = message.text.strip().lower()
    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={info_city}&appid={api}&units=metric')
    data = json.loads(req.text)
    bot.reply_to(message, f'Зараз погода: {data["main"]["temp"]}')



bot.polling(non_stop=True)

