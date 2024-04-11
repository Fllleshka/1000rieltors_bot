from telebot import *
import time


botkey = "6782872811:AAE0Mp5KOp4VrSHQc0J1ENy2bML75AIMIck"

# Токен для связи с ботом
bot = telebot.TeleBot(botkey)

# Командa start(Приветственное сообщение)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    textmessage = "Привет, {0.first_name}"
    msg = bot.reply_to(message, textmessage.format(message.from_user))
    select_ownership_type(message, bot)

# Запуск первого шага
def select_ownership_type(message, bot):
    try:
        image = r"robot_firststep.jpeg"
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_one = telebot.types.KeyboardButton("🏢Аренда🏢")
        button_second = telebot.types.KeyboardButton("🏡Покупка🏡")
        markup.add(button_one, button_second)
        textmessage = """🏘Приветствую вас в нашем боте по подбору недвижимости!🏘\n\nМеня зовут 🤖[Имя бота]🤖, и я готов помочь вам найти идеальное место.\nПросто укажите свои предпочтения, и мы подберем для вас лучшие варианты.\nДля начала работы воспользуйтесь кнопками меню или напишите ✍️ мне, что вас интересует.\n\nПоехали 🚚 искать оптиманое решение вашей проблемы!"""
        bot.send_photo(message.chat.id, photo=open(image, 'rb'), caption=textmessage)
        textmessage = "🔽Выберите одну из кнопок ниже🔽"
        bot.send_message(message.chat.id, textmessage, reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так на первом шаге(')

# Обработка кнопок
@bot.message_handler(content_types= ['text'])
def select_placement_type(message):
    match (message.text):
        # Кнопки для клиентов
        case "🏢Аренда🏢":
            textmessage = "Хорошо, {0.first_name}.\nВы выбрали Аренду помещения.\nПожалуйста выберите тип помещения, которое планируете арендовать."
            bot.reply_to(message, textmessage.format(message.from_user))
            select_place_type(message, "арендовать")
        case "🏡Покупка🏡":
            textmessage = "Хорошо, {0.first_name}.\nВы выбрали Покупку помещения.Пожалуйста выберите тип помещения, которое планируете покупать."
            bot.reply_to(message, textmessage.format(message.from_user))
            select_place_type(message, "покупать")
        case "Офисное помещение":
            textmessage = "Отлично, {0.first_name}.\nВы выбрали Офисное помещение.\nОсталась всего 2 шага."
            bot.reply_to(message, textmessage.format(message.from_user))
        case "Торговое помещение":
            textmessage = "Отлично, {0.first_name}.\nВы выбрали Торговое помещение.\nОсталась всего 2 шага."
            bot.reply_to(message, textmessage.format(message.from_user))
        case "Производственное помещение":
            textmessage = "Отлично, {0.first_name}.\nВы выбрали Производственное помещение.\nОсталась всего 2 шага."
            bot.reply_to(message, textmessage.format(message.from_user))
        case "Складское помещение":
            textmessage = "Отлично, {0.first_name}.\nВы выбрали Складское помещение.\nОсталась всего 2 шага."
            bot.reply_to(message, textmessage.format(message.from_user))

def select_place_type(message, type_placement):
    try:
        image = r"robot_firststep.jpeg"
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_one = telebot.types.KeyboardButton("Офисное помещение")
        markup.add(button_one)
        button_second = telebot.types.KeyboardButton("Торговое помещение")
        markup.add(button_second)
        button_third = telebot.types.KeyboardButton("Производственное помещение")
        markup.add(button_third)
        button_fourth = telebot.types.KeyboardButton("Складское помещение")
        markup.add(button_fourth)
        textmessage = "Пожалуйста выберите тип помещения, которое планируете " + str(type_placement) + "."
        bot.send_message(message.chat.id, textmessage, reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так на первом шаге(')


print("Бот запущен!")
while True:
    try:
        # Запустили постоянный опрос бота Telegram
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(15)