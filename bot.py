from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    updater = Updater("536305288:AAGTKLPlZytJlj-QUQFnlJgf0h8aKleZQ0E")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def get_constellation(bot, update, args):
    planet = ''.join(args).capitalize()
    
    d = datetime.datetime.now()
    today = d.strftime('%Y/%m/%d')

    ephem_planet = getattr(ephem, planet)
    ephem_planet_date = ephem_planet(today)

    constellation = ephem.constellation(ephem_planet_date)[1]
    update.message.reply_text(constellation)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

main()