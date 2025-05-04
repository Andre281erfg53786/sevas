import telebot 
import keyboards
BOT_TOKEN = '7740470916:AAEqWao7o1IdaL-dtnta99HS8gj6KR6nmVI' 
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text = message.text
    if msg_text == 'Фото' :
        bot.send_message(message.chat.id, text='Ввидете описание фото.' , reply_markup=keyboards.BackKeyboard)
    elif msg_text == 'Текст' :
        bot.send_message(message.chat.id, text='Общайся со мной' , reply_markup=keyboards.BackKeyboard)
    elif msg_text == 'Назад' :
        bot.send_message(message.chat.id, text='Главное меню' , reply_markup=keyboards.MainKeyboard)
    else :
        bot.send_message(message.chat.id, text='Главное меню' , reply_markup=keyboards.MainKeyboard)
        
bot.polling()