from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/режим_работы')
b2 = KeyboardButton('/номер')
b3 = KeyboardButton('/меню')
b4 = KeyboardButton('/место')
#b5 = KeyboardButton('/мой номер', request_contact=True) - дать контакт USERA!
#b6 = KeyboardButton('/отправить где я', request_location=True) - дать локацию USERA!


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2, b3, b4)#.add(b5)#.insert(b6)#ТАКЖЕ .add только в столбик, .insert располагает 2 внизу 1 сверху
