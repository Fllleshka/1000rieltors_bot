from telebot import *
import time


botkey = "6782872811:AAE0Mp5KOp4VrSHQc0J1ENy2bML75AIMIck"

# Токен для связи с ботом
bot = telebot.TeleBot(botkey)

# Командa start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    textmessage = "Привет, {0.first_name}"
    msg = bot.reply_to(message, textmessage.format(message.from_user))
    process_name_step(message, bot)

def process_name_step(message, bot):
    try:
        image = r"robot_firststep.jpeg"
        textmessage = """🏘Приветствую вас в нашем боте по подбору недвижимости!🏘\n\nМеня зовут 🤖[Имя бота]🤖, и я готов помочь вам найти идеальное место.\nПросто укажите свои предпочтения, и мы подберем для вас лучшие варианты.\nДля начала работы воспользуйтесь кнопками меню или напишите ✍️ мне, что вас интересует.\n\nПоехали 🚚 искать оптиманое решение вашей проблемы!\n\n🔽Выберите одну из кнопок ниже🔽"""
        bot.send_photo(message.chat.id, photo=open(image, 'rb'), caption=textmessage)        
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так')



print("Бот запущен!")
while True:
    try:
        # Запустили постоянный опрос бота Telegram
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(15)