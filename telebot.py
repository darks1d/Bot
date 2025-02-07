import telebot 
import parser
TOKEN = "7709523457:AAGdkIBWgJd0ZQXI9Q_5QZElVDllElTiE_4"
bot = telebot.TeleBot
@bot.message_handler(commandes=['start', 'go'])
def start_handler(massage):
        bot.send_message(message.chat.id,'Приве я который выдает загатки')
bot.polling()
@bot.messange_handler(content_types=['text])
def text_handler(message):
 text = message.text.lower()
 chad_id = message.chat.id
 if text == "привет":
  bot.send_message(chad_id,)
 elfi text == ""
  bot.send_message(chad_id'')
 else:
  bot.send_message(chad_id'')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def start(update: Update, context: CallbackContext) -> None:update.message.reply_text('Привет! Я ваш бот.')
def help_command(update: Update, context: CallbackContext) -> None:update.message.reply_text('Помощь: используйте /start для начала.')
def main() -> None:
dispatcher = updater.dispatcher
 dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
