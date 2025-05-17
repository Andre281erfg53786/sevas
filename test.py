import telebot 
import keyboards
import fsm

BOT_TOKEN = '7740470916:AAEqWao7o1IdaL-dtnta99HS8gj6KR6nmVI' 
starter = fsm.FSM()
bot = telebot.TeleBot(BOT_TOKEN)






@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text = message.text
    state = starter.get_state(message.chat.id)
    
    if state == fsm.DEFULT_STATE:
        hadel_default_state(message)
    elif state == fsm.IMAGE_STATE:
        hadel_image_state(message)
    elif state == fsm.TEXT_STATE:
        hadel_text_state(message)
    else:
        return_to_menu(message.chat.id)


    def return_to_menu (chat.id):
        starter.set_state(message.chat.id , fsm.DEFULT_STATE)
        bot.send_message(message.chat.id, text='Ввидете описание фото.' , reply_markup=keyboards.MainKeyboard)



    def hadel_default_state(message)  :
        if msg_text == 'Фото' :
            starter.set_state(message.chat.id , fsm.IMAGE_STATE)
            bot.send_message(message.chat.id, text='Ввидете описание фото.' , reply_markup=keyboards.BackKeyboard)
        elif msg_text == 'Текст' :
            starter.set_state(message.chat.id , fsm.TEXT_STATE)
            bot.send_message(message.chat.id, text='Общайся со мной' , reply_markup=keyboards.BackKeyboard)
        else:
            return_to_menu(message.chat.id)

    def hadel_image_state (message):
        if msg_text == 'Назад' :
            return_to_menu(message.chat.id)
        else:
            bot.send_message(message.chat.id, text='Скоро будет генирация фото...' )

    def hadel_text_state (message):
        if msg_text == 'Назад' :
            return_to_menu(message.chat.id)
        else:
            bot.send_message(message.chat.id, text='Скоро будет генирация ъэ...' )







            
bot.polling()