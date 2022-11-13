import telebot
import pyowm
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'en'
owm = pyowm.OWM('b3e82e0476f5a3633713f2c5bc95be81', config_dict)
bot = telebot.TeleBot("5429028163:AAFCvziFF0woW_G2YrNKKtLptVpjSME2N6M")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Hello, ' + str(message.from_user.first_name) + ',\n/start - To start bot\n/help - Comands of bot\nTo find out the weather just type your city.')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '/start - To start bot\n/help - Comands of bot\nTo find out the weather just type your city.')

@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        t = w.temperature("celsius") 
        temp = t['temp']
        temp2 = t['feels_like']
        temp3 = t['temp_max']
        temp4 = t['temp_min']

        output = "In the " + message.text.capitalize() + " now is " + w.detailed_status + ".\n"
        output += "The temperature is currently " + str(temp) + "°C that feels like " + str(temp2) + "°C.\n"
        output += "Today's maximum is " + str(temp3) + "°C and minimum " + str(temp4) + "°C.\n" 

        if temp < 10:
            output += "Wow that seems like pretty cold outside, you should wear something warm."
        elif temp < 20:
            output += "It's not cold but also not hot. Don't forget to take a jacket just in case."
        else:
            output += "What are you waiting for? Go outside and do something! Such good weather does not happen every day!"

        bot.send_message(message.chat.id, output)
    except:
        bot.send_message(message.chat.id,"Couldn't find this city! Try again.")

bot.polling(non_stop=True)