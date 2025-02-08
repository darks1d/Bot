from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Список загадок и ответов
riddles = [
    {"question": "Что можно увидеть с закрытыми глазами?", "answer": "сон"},
    {"question": "Что идет, не двигаясь с места?", "answer": "часы"},
    {"question": "Чем больше из нее берешь, тем больше она становится. Что это?", "answer": "яма"},
    {"question": "Висит груша — нельзя скушать. Что это?", "answer": "лампочка"},
    {"question": "Что принадлежит вам, но другие используют это чаще, чем вы?", "answer": "имя"},
]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот-загадочник. Напиши /riddle, чтобы получить загадку.")

def riddle(update: Update, context: CallbackContext):
    riddle_data = random.choice(riddles)
    question = riddle_data["question"]
    context.user_data["current_answer"] = riddle_data["answer"] 
    update.message.reply_text(f"Загадка: {question}")

def handle_message(update: Update, context: CallbackContext):
    user_answer = update.message.text.lower()
    correct_answer = context.user_data.get("current_answer", "")

    if user_answer == correct_answer:
        update.message.reply_text("Правильно! Молодец! 🎉 Напиши /riddle для новой загадки.")
    else:
        update.message.reply_text("Неверно. Попробуй еще раз!")

def main():
    TOKEN = "7709523457:AAGdkIBWgJd0ZQXI9Q_5QZElVDllElTiE_4"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("riddle", riddle))
        
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


