import types

import telebot

bot = telebot.TeleBot('1226823066:AAFZAVW9NUdKSoXL_RYKLse1clfeV_1E3ks')  # подключим бота


@bot.message_handler(content_types=['text', 'audio', 'document'])  # метод получения текстовых сообщений
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text.lower() == '/help':
        bot.send_message(message.from_user.id, 'Напиши Привет)')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши /help')


name = ''
surname = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Тебя зовут ' + name + ' ' + surname + '?')


bot.polling(none_stop=True, interval=0)  # мониторит кто что написал
