import json, string
from create_bot import dp
from aiogram import types, Dispatcher


#@dp.message_handler()
async def echo_send(message:types.Message):
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('маты запрещены')
        await message.delete()

def register_handlers_ofher(dp: Dispatcher):
    dp.register_message_handler(echo_send)