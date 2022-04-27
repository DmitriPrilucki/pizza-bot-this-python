from aiogram import types
from create_bot import dp, bot
from aiogram import Dispatcher
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=["режим_работы"])
async def work(message: types.Message):
    await bot.send_message(message.from_user.id, 'С 0:00 до 23:59')

# @dp.message_handler(commands=["номер"])
async def phone(message: types.Message):
    await bot.send_message(message.from_user.id, 'Какойто номер')

# @dp.message_handler(commands=['start', 'help'])
async def comand(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'приятного аппетита!', reply_markup=kb_client)
        # await message.delete() удоление сообщения
    except:
        await message.reply("общение с ботом в ЛС:\nhttps://t.me/Redly_tst_bot")


# @dp.message_handler(commands=["место"])
async def work_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул хлебобулочная д 5689')



# @dp.message_handler(commands=["меню"])
async def menu_pizza(message: types.Message):
    await sqlite_db.sql_read(message)

#Важен порядок!Если work и phone поменять местами то ничё не выполница! Тоесть если в коде "режим_работы" первый то и в
#register_handlers_client он первый!
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(work, commands=['режим_работы'])
    dp.register_message_handler(phone, commands=['номер'])
    dp.register_message_handler(comand, commands=['start', 'help'])
    dp.register_message_handler(work_place, commands=["место"])
    dp.register_message_handler(menu_pizza, commands=["меню"])

