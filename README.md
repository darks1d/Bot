pip install pyTelegramBotAPI==4.26.0i
import logging 
from telegram import Update
from telegram.exe import Update,  CommandHanler, CallbackContext
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def start(update: Update, context: CallbackContext) -> None:update.message.reply_text('Привет! Я ваш бот.')
def help_command(update: Update, context: CallbackContext) -> None:update.message.reply_text('Помощь: используйте /start для начала.')
def main() -> None:
updater = Updater("YOUR_TOKEN_HERE")
dispatcher = updater.dispatcher
 dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
