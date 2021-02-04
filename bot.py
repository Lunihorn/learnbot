
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

#                          дата собития, уровень события и сообщение
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )



def greet_user(bot, update):
    text = ('Привет')
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, - Chat id: %s, - Message: %s", update.message.chat.username, 
                 update.message.chat.id, update.message.text)
    logging.info(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.TG_API_KEY, use_context=False)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
 





















































