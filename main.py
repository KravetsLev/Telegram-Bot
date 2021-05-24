import telebot
import config
import random
from buttons import *
from dbhelper import DBHelper


bot = telebot.TeleBot(config.TOKEN, parse_mode='html')
db = DBHelper()


@bot.message_handler(commands=['start', 'hello', 'laugh'])
def commands_handler(m):
    if m.text == '/start':
        bot.send_message(m.chat.id, 'привіт холоп' )
    elif m.text == '/hello':
        bot.send_message(m.chat.id, 'привіт холоп ' + m.from_user.first_name)
    elif m.text == '/laugh':
        bot.send_message(m.chat.id, 'ХАХХАХАХ')

@bot.message_handler(commands=['stop'])
def commands_handler(m):
    bot.send_message(m.chat.id, 'пака мудєра' )

@bot.message_handler(commands=['namebot'])
def commands_handler(m):
    bot.send_message(m.chat.id, 'бот називається bot' )

@bot.message_handler(commands=['help'])
def help_command(message):
    # keyboard
    markup = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.KeyboardButton("Random")
    button_2 = telebot.types.KeyboardButton("Weather")
    button_3 = telebot.types.KeyboardButton("💋")
    button_4 = telebot.types.KeyboardButton("math")
    button_5 = telebot.types.KeyboardButton("Where?")
    button_6 = telebot.types.KeyboardButton('🦷')

    markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, f"How can I help you {message.from_user.first_name} ?", reply_markup=markup)


@bot.message_handler(commands=['list'])
def list_command(message):
    items = db.get_items()
    text = ""
    for item in items:
        text = text + str(item) + '\n'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['my_list'])
def my_list_command(message):
    bot.send_message(message.chat.id, message.from_user.first_name + ' ' + message.from_user.last_name)
    chat = message.chat.id
    items = db.filter_items(chat)

    text = ""
    for item in items:
        text = text + str(item) + '\n'

    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def text_message(message):

    text = message.text
    chat = message.chat.id
    db.add_item(text, chat)

    if message.text == 'Random':
        bot.send_message(message.chat.id, str(random.randint(1, 12)))
    elif message.text == 'Weather':
        catch_weather(bot, message)
    elif message.text == '💋':
        catch_kiss(bot, message)
    elif message.text == 'math':
        catch_math(bot, message)
    elif message.text == 'Where?':
        catch_where(bot, message)
    elif message.text == '🦷':
        catch_tooth(bot, message)
    else:
        bot.send_message(chat, "Sorry, I don't understand you")


def main():

    db.setup()


    bot.polling(none_stop=True)


if __name__ == '__main__':

    main()
