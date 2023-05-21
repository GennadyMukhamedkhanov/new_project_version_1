import time
import telebot
import poetry
import counting
import random
from telebot import types
You = 0
BOT = 0
count_you = 0
count_bot = 0
TOKEN = "6292419420:AAHss-etOCeORRrkkqapCQgRxKSkrFtJXAg"
bot = telebot.TeleBot(TOKEN)


answers = {'как дела?': 'У меня все хорошо!', 'как тебя зовут?': 'Меня зовут Telebot )))',
           'какой сегодня год?': 'Сейчас 2023 год', 'кто тебя создал?': 'Меня создал какой-то хороший паренек'}


@bot.message_handler(commands=['start'])
def help(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='/list')
    btn2 = types.KeyboardButton(text='/foto')
    btn3 = types.KeyboardButton(text='/video')
    btn4 = types.KeyboardButton(text='/play')
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Погнали...', reply_markup=kb)


@bot.message_handler(commands=['video'])
def help(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Ютуб', url='https://www.youtube.com/')
    btn2 = types.InlineKeyboardButton(text='Яндекс', url='https://ya.ru/video/')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Видео', reply_markup=kb)


@bot.message_handler(commands=['list'])
def help(message):
    bot.send_message(message.chat.id, '<b>Список всех вопросов к боту:</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<i>как меня зовут?</i>', parse_mode='HTML')
    for i in answers:
        bot.send_message(message.chat.id, f'<i>{i}</i>', parse_mode='HTML')


@bot.message_handler(commands=['foto'])
def foto(message):
    #file = open("templates/foto.png", 'rb')
    #bot.send_photo(message.chat.id, file, 'Это фото')
    # или так:
    bot.send_photo(message.chat.id, r'https://vsegda-pomnim.com/uploads/posts/2022-04/1649112612_32-vsegda-pomnim-com-p-chudesnii-mir-prirodi-foto-35.jpg', 'Это тоже фото')
    #file.close()


# Callback кнопки
@bot.message_handler(commands=['play'])
def foto(message):
    if message.from_user.id == 241468532:
        kb = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text='🪨', callback_data='btn1')
        btn2 = types.InlineKeyboardButton(text='✂️', callback_data='btn2')
        btn3 = types.InlineKeyboardButton(text='📃', callback_data='btn3')
        count = types.InlineKeyboardButton(text='Общий счет🧮', callback_data='count')
        count_my = types.InlineKeyboardButton(text='Мой счет🧮', callback_data='count_my')
        reset = types.InlineKeyboardButton(text='Сброс общего счета всех игроков', callback_data='resen')
        reset_my = types.InlineKeyboardButton(text='Сброс счета моей игры', callback_data='resen_my')
        kb.add(btn1, btn2, btn3, count, count_my, reset, reset_my)
        bot.send_message(message.chat.id, 'Игра камень ножницы бумага', reply_markup=kb)
    else:
        kb = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text='🪨', callback_data='btn1')
        btn2 = types.InlineKeyboardButton(text='✂️', callback_data='btn2')
        btn3 = types.InlineKeyboardButton(text='📃', callback_data='btn3')
        count = types.InlineKeyboardButton(text='Общий счет🧮', callback_data='count')
        count_my = types.InlineKeyboardButton(text='Мой счет🧮', callback_data='count_my')
        #reset = types.InlineKeyboardButton(text='Сброс общего счета всех игроков', callback_data='resen')
        reset_my = types.InlineKeyboardButton(text='Сброс счета моей игры', callback_data='resen_my')
        kb.add(btn1, btn2, btn3, count, count_my, reset_my)
        bot.send_message(message.chat.id, 'Игра камень ножницы бумага', reply_markup=kb)


list_of_clients = []

@bot.callback_query_handler(func=lambda call: call.data)
def callback(call):
    global You, BOT, count_you, count_bot

    if call.message:
        if call.data == 'btn1':
            stone = counting.count('камень')
            if stone == 'Ты выиграл':
                You += 1
                count_you += 1
            elif stone == 'Выиграл БОТ':
                BOT += 1
                count_bot += 1
            bot.send_message(call.message.chat.id, stone)
        elif call.data == 'btn2':
            scissors = counting.count('ножницы')
            if scissors == 'Ты выиграл':
                You += 1
                count_you += 1
            elif scissors == 'Выиграл БОТ':
                BOT += 1
                count_bot += 1
            bot.send_message(call.message.chat.id, scissors)
        elif call.data == 'btn3':
            paper = counting.count('бумага')
            if paper == 'Ты выиграл':
                You += 1
                count_you += 1
            elif paper == 'Выиграл БОТ':
                BOT += 1
                count_bot += 1
            bot.send_message(call.message.chat.id, paper)
        elif call.data == 'count':
            bot.send_message(call.message.chat.id, f'Общее колличество очков у играков: {You} ')
            bot.send_message(call.message.chat.id, f'Общее колличество очков у бота: {BOT}')
        elif call.data == 'count_my':
            bot.send_message(call.message.chat.id, f'У вас очков: {count_you} ')
            bot.send_message(call.message.chat.id, f'У бота очков: {count_bot}')
        elif call.data == 'resen':
            You = 0
            BOT = 0
        elif call.data == 'resen_my':
            count_you = 0
            count_bot = 0


@bot.message_handler()
def help(message):
    if message.text.lower() in answers.keys():
        bot.reply_to(message, answers[message.text.lower()])
    elif message.text.lower() == 'как меня зовут?':
        bot.reply_to(message, f'Тебя зовут {message.from_user.first_name} ')
    elif message.text.lower() == 'стихи':
        # Todo перенести рандом в функцию что бы стих выдавался вызовом функции
        t = random.randint(1, 5)
        bot.reply_to(message, poetry.st(t))
    else:
        bot.send_message(message.chat.id, "Такого вопроса нет в моем списке")
        bot.send_message(message.chat.id, "Введи команду /start или /list и посмотрите перечеть запросов")
        bot.send_message(message.chat.id, "Введи команду /foto и посмотрите фото")
        bot.send_message(message.chat.id, "Игра выбери /play")
        bot.send_message(message.chat.id, "Либо напишите запрос 'стихи' и насладитесь поэзией")


while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка {e}")
        time.sleep(15)