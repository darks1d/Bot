from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Списки загадок по сложности
riddles_easy = [
    {"question": "Что можно увидеть с закрытыми глазами?", "answer": "сон"},
    {"question": "Что идет, не двигаясь с места?", "answer": "часы"},
]

riddles_medium = [
    {"question": "Чем больше из нее берешь, тем больше она становится. Что это?", "answer": "яма"},
    {"question": "Висит груша — нельзя скушать. Что это?", "answer": "лампочка"},
]

riddles_hard = [
    {"question": "Что принадлежит вам, но другие используют это чаще, чем вы?", "answer": "имя"},
    {"question": "Что можно сломать, даже если это не трогать?", "answer": "обещание"},
]

def start(update: Update, context: CallbackContext):
    
    keyboard = [
        [InlineKeyboardButton("Начать игру", callback_data='start_game')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Привет! Я бот-загадочник. Нажми на кнопку, чтобы начать.", reply_markup=reply_markup)

def start_game(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Легкий уровень", callback_data='easy')],
        [InlineKeyboardButton("Средний уровень", callback_data='medium')],
        [InlineKeyboardButton("Сложный уровень", callback_data='hard')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text("Выбери уровень сложности:", reply_markup=reply_markup)

def choose_level(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    level = query.data
    context.user_data["level"] = level

    send_riddle(update, context)

def send_riddle(update: Update, context: CallbackContext):
    level = context.user_data.get("level")

    if level == "easy":
        riddle_data = random.choice(riddles_easy)
    elif level == "medium":
        riddle_data = random.choice(riddles_medium)
    elif level == "hard":
        riddle_data = random.choice(riddles_hard)
    else:   
        riddle_data = random.choice(riddles_easy)

    question = riddle_data["question"]
    context.user_data["current_answer"] = riddle_data["answer"]  

    if update.callback_query:
        update.callback_query.edit_message_text(f"Загадка: {question}")
    else:
        update.message.reply_text(f"Загадка: {question}")

# Обработка ответа пользователя
def handle_message(update: Update, context: CallbackContext):
    user_answer = update.message.text.lower()
    correct_answer = context.user_data.get("current_answer", "")

    if user_answer == correct_answer:
        update.message.reply_text("Правильно! Молодец! 🎉 Напиши /start для новой загадки.")
    else:
        update.message.reply_text("Неверно. Попробуй еще раз!")

def main():

    TOKEN = "7709523457:AAGdkIBWgJdOzqXI9Q_5qzelVDllElTiE_4"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CallbackQueryHandler(start_game, pattern='start_game'))
    dispatcher.add_handler(CallbackQueryHandler(choose_level, pattern='^(easy|medium|hard)$'))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    logger.info("Бот запущен")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
