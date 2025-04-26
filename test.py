import telebot 
BOT_TOKEN = '7740470916:AAEqWao7o1IdaL-dtnta99HS8gj6KR6nmVI' 
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()