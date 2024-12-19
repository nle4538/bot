from telebot import types
import telebot
import os

#API_TOKEN = "7750297044:AAFmP7a35CK5l-9uDiEtXixSRFOz9NqUJFE"
API_TOKEN =  os.environ.get('TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, давай решу""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: message.text == 'calc')
def echo_message(message):
    try:

        expression = message.text.strip()

        result = eval(expression)

        bot.reply_to(message, f"Результат: {result}")

    except Exception as e:
        bot.reply_to(message,
                     "Произошла ошибка при выполнении вычисления. Проверьте правильность ввода и попробуйте снова.")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("? Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)

bot.infinity_polling()
