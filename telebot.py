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


