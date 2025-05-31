import telebot 
import keyboards
import fsm
import ai
import loguru
import yaml
import sys

logger = loguru.

try:
     with open("./config.yaml" , 'r') as file:
          cfg = yaml.safe_load(file)
          logger.inf('Успешно загружаем конфиг')
except Exception as e:
     logger.warning('Произошла ошибка при загрузке конфига ({})' , str(e))
     sys.exit(1)

BOT_TOKEN = cfg['telegram_token']
starter = fsm.FSM()
ai_service = ai.AI(cfg)
bot = telebot.TeleBot(BOT_TOKEN)


def return_to_menu (chat_id):
        starter.set_state(chat_id , fsm.DEFULT_STATE)
        bot.send_message(chat_id, text='Ввидете описание фото.' , reply_markup=keyboards.MainKeyboard)

def hadel_default_state(message)  :
        if message.text == 'Фото' :
            starter.set_state(message.chat.id , fsm.IMAGE_STATE)
            bot.send_message(message.chat.id, text='Ввидете описание фото.' , reply_markup=keyboards.BackKeyboard)
        elif message.text == 'Текст' :
            starter.set_state(message.chat.id , fsm.TEXT_STATE)
            bot.send_message(message.chat.id, text='Общайся со мной' , reply_markup=keyboards.BackKeyboard)
        else:
            return_to_menu(message.chat.id)

def hadel_image_state (message):
        if message.text == 'Назад' :
            return_to_menu(message.chat.id)
        else:
            try:
                 msg = bot.send_message(chat_id=message.chat.id , text = 'Генерируем...')
                 image_url = ai_service .generate_image(message.text)
                 bot.delete_message(chat_id=message.chat.id, message_id=msg.id )
                 bot.send_photo(chat_id=message.chat.id, caption='Ваше фото' , photo=image_url)
            except Exception as e:
                 bot.send_message(chat_id=message.chat.id, text=f'Произоша ошибка ({str(e)})')

def hadel_text_state (message):
        if message.text == 'Назад' :
            ai_service.clear_dialog(message.chat.id)
            return_to_menu(message.chat.id)
        else:
            msg = bot.send_message(message.chat.id ,  'Думаю над запросом...')
            txt = ai_service.generate_text(message.text , message.chat.id )
            msg = bot.edit_message_text(text=txt , chat_id=message.chat.id , message_id=msg.id )

        
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text = message.text
    state = starter.get_state(message.chat.id)
    
    logger.info(
        "Пользователь [ {} : {}] отправил сообщение '{}' в состоянии {}" ,
         message.chat.id,
         message.from_user.first_name,
         message.text,
         state
    )


    if state == fsm.DEFULT_STATE:
        hadel_default_state(message)
    elif state == fsm.IMAGE_STATE:
        hadel_image_state(message)
    elif state == fsm.TEXT_STATE:
        hadel_text_state(message)
    else:
        return_to_menu(message.chat.id)

            
bot.polling()