from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(update, context):
    buttons = [
        [
            InlineKeyboardButton('Private', url='https://t.me/AvazbekDev_admin_bot')
        ],
        [
            InlineKeyboardButton('Tg Channel', url='https://t.me/avazbekcoder'),
            InlineKeyboardButton('Programming', url='https://t.me/FullStackExpress')
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="↗️ @avazbekcoder - Tizimlar ro'yxati!", reply_markup=keyboard)


def button_callback(update, context):
    query = update.callback_query
    query.answer() # Optional: send a response to the user
    # Handle the callback here, e.g., redirect to another channel


def main():
    updater = Updater('6953213974:AAHQKdO3Ob6-ArG-Jy836IQ-eNGYRHIFRvE', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback)) # Add the callback handler
    updater.start_polling()
    updater.idle()


main()