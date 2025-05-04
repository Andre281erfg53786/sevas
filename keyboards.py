import telebot
button1 = telebot.types.KeyboardButton(text='Назад')
button2 = telebot.types.KeyboardButton(text='Фото')
button3 = telebot.types.KeyboardButton(text='Текст')

BackKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
MainKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

BackKeyboard.add(button1)
MainKeyboard.add(button2, button3)