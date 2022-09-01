from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram import *
from telegram.ext import *
from telegram.chat import *
from client import send_payload

with open("tokenIOT.txt", "r") as f_:
    TOKEN = f_.readline()

updater = Updater(TOKEN, use_context=True)
update = Update

light = False


# x1 = threading.Thread(target=talk, args="On")
# x2 = threading.Thread(target=talk, args="Off")


def start(update: Update, context: CallbackContext):
    username = context.bot.get_chat(chat_id=update.effective_chat.id)
    message = f"""Hello {username.username}!!!
    Welcome, Ready to play around with some LEDs?!
    /help - confused??🤔"""
    context.bot.send_message(chat_id= update.effective_chat.id, text=message)
    

def help_(update: Update, context: CallbackContext):
    con_t = '''/yes - proceed to LED control grid
    /no - end session
    /cancel - end session
    Just tap "On" to turn on the LED and vice versa😁'''
    context.bot.send_message(chat_id=update._effective_chat.id, text=con_t)

def yes(update: Update, context: CallbackContext):
    username = context.bot.get_chat(chat_id=update.effective_chat.id)
    buttons = [[KeyboardButton("On"), KeyboardButton("Off")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Good choice {username.username}!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    user_input = update.message.text
    user__ = list(user_input)
    if user_input == 'On':
        message = "Let there be light!!!🔥"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        light = True
        print(light)
        send_payload(user_input)
    elif user_input == 'Off':
        message = "Light Off!😒"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        light = False
        print(light)
        send_payload(user_input)
    elif user__[0] != "/" and user_input != "On" and user_input != "Off":
        message = "English please😑"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def fetch_payload(update: Update, context: CallbackContext):
    user_input = update.message.text
    user__ = list(user_input)
    
    if user_input == 'On':
        message = "Let there be light!!!🔥"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        light = "On"
        print(light)
        send_payload(user_input)
    elif user_input == 'Off':
        message = "Light Off!😒"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        light = "Off"
        print(light)
        send_payload(user_input)
        

    elif user__[0] != "/" and user_input != "On" and user_input != "Off":
        message = "English please😑"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)






if __name__ == "__main__":
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help_))
    updater.dispatcher.add_handler(CommandHandler('yes', yes))
    updater.dispatcher.add_handler(MessageHandler(Filters.update, fetch_payload))
    
    
    
    updater.start_polling()
    updater.idle()