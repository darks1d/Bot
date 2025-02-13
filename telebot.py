from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

riddles_easy = [
    {"question": "Что можно увидеть с закрытыми глазами?", "answer": "сон"},
    {"question": "Что идет, не двигаясь с места?", "answer": "часы"},
    {"question": "Он сейчас везде и всюду,без него не могут люди,если вдруг его не станет,в мире паника настанет?", "answer": "Интернет"},
    {"question": "Темная, большая,по небу летает?", "answer": "Туча"},
    {"question": "Кислый и противный плод,на деревьях он растёт?", "answer": "Лимон"},
    {"question": "За зубами он сидит,мне слова он говорит?", "answer": "Язык"},
    {"question": "С двух сторон на голове,любят они слушать?", "answer": "Уши"}
]

riddles_medium = [
    {"question": "Чем больше из нее берешь, тем больше она становится что это?", "answer": "яма"},
    {"question": "Висит груша — нельзя скушать. Что это?", "answer": "лампочка"},
    {"question": "Как можно одновременно увидеть Австралию и Америку?", "answer": "На карте"},
    {"question": "Оно может повторить любое движение, но никогда не придумает ничего нового?", "answer": "Зеркало"},
    {"question": "Что на свете, легкое, как снежинка, а не удерживается и пяти минут?", "answer": "Дыхыние"},
    {"question": "Если их много — то вес стремиться к нулю?", "answer": "Дырки"},
]

riddles_hard = [
    {"question": "Что принадлежит вам, но другие используют это чаще, чем вы?", "answer": "имя"},
    {"question": "Что можно сломать, даже если это не трогать?", "answer": "обещание"},
    {"question": "Что можно измерить, но нельзя увидеть или потрогать?", "answer": "Время"},
    {"question": "Есть три литра кефира. Как его уместить в литровую банку?", "answer": "Сварить творог"},
    {"question": "Оно может говорить, но точно ничего не покажет?", "answer": "Радио"},
    {"question": "Она везде: в почве, в небе, в воздухе, в реке, в море, в овощах, во фруктах и даже в человеке?", "answer": "Вода"},
    {"question": "Они ведут нас вперед, хотя сами всегда ходят по кругу?", "answer": "Стрелки на часах"},
    {"question": "Как спрыгнуть с лестницы высотного здания,чтоб не было переломов и с жизнью прощания?", "answer": "Надо прыгать с самой нижней ступени"},
]

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Начать игру", callback_data='start_game')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Привет! Я бот-загадочник. Нажми на кнопку, чтобы начать.", reply_markup=reply_markup)

async def start_game(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Легкий уровень", callback_data='easy')],
        [InlineKeyboardButton("Средний уровень", callback_data='medium')],
        [InlineKeyboardButton("Сложный уровень", callback_data='hard')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("Выбери уровень сложности:", reply_markup=reply_markup)

async def choose_level(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    level = query.data
    context.user_data["level"] = level
    context.user_data["used_riddles"] = []

    await send_riddle(update, context)

async def send_riddle(update: Update, context: CallbackContext):
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
        await update.callback_query.edit_message_text(f"Загадка: {question}")
    else:
        await update.message.reply_text(f"Загадка: {question}")

async def handle_message(update: Update, context: CallbackContext):
    user_answer = update.message.text.lower()
    correct_answer = context.user_data.get("current_answer", "")

    if user_answer == correct_answer:
        keyboard = [
            [InlineKeyboardButton("Выбрать уровень сложности", callback_data='start_game')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Правильно! Молодец! 🎉", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Неверно. Попробуй еще раз!")

def main():

    TOKEN = "7709523457:AAGdkIBWgJdOzqXI9Q_5qzelVDllElTiE_4"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CallbackQueryHandler(start_game, pattern='start_game'))
    application.add_handler(CallbackQueryHandler(choose_level, pattern='^(easy|medium|hard)$'))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Бот запущен")
    application.run_polling()

if __name__ == '__main__':
    main()
