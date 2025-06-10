import telebot
import requests
import json
bot=telebot.TeleBot('7759941665:AAGwaTMgWDiGuqARz42dLeOHThIGnA4ehPs')
API = 'f20888227f2d2440ebf6b9dfdef5f811'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}°C')
    else:
        bot.reply_to(message, 'Город указан неверно')

































#@bot.message_handler(commands=['me'])
#def start(message):
    #bot.send_message(message.chat.id, f'{message.from_user.first_name} 'f'ID:{message.from_user.id}')



#@bot.message_handler()
#def info(message):
    #markup = types.InlineKeyboardMarkup()
    #markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    #markup.add(types.InlineKeyboardButton('Удалить сообщение', callback_data='delete'))
    #markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    #if message.text.lower()== 'привет':
        #bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)
    #elif message.text.lower() == 'id':
        #bot.reply_to(message, f'ID: {message.from_user.id}')

#@bot.callback_query_handler(func=lambda callback: True)
#def callback_message(callback):
    #if callback.data == 'delete':
        #bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    #elif callback.data == 'edit':
        #bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



bot.infinity_polling()