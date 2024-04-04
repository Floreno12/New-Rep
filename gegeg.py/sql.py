import telebot
from telebot import types
import sqlite3

# TOKEN = '6546548054:AAGpWFtLMD-y0yY5D6RNFAEa2-8uQe9jqU'
bot = telebot.TeleBot(TOKEN)
name = None

@bot.message_handler(commands=['start'])
def get_start(message):
    conne = sqlite3.connect('project.sql')
    curso = conne.cursor()

    curso.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, pass TEXT)')
    conne.commit()
    curso.close()
    conne.close()
    bot.send_message(message.chat.id, 'Register yourself')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Write your password')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conne = sqlite3.connect('project.sql')
    curso = conne.cursor()

    curso.execute(f'INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
    conne.commit()
    curso.close()
    conne.close()
    
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('List users', callback_data='users')
    markup.add(btn)

    bot.send_message(message.chat.id, 'You are registered!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'users':
        conne = sqlite3.connect('project.sql')
        curso = conne.cursor()
        curso.execute('SELECT * FROM users')
        users = curso.fetchall()
        conne.close()

        users_list = "\n".join([f"{user[1]}: {user[2]}" for user in users])

        bot.send_message(call.message.chat.id, f'List of users:\n{users_list}')

bot.polling(non_stop=True)
