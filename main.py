
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db




async def on_startup(_):
    print("бот василий")
    sqlite_db.sql_start()

from handlers import client, ofher, admin

admin.register_handler_admin(dp)
client.register_handlers_client(dp)
ofher.register_handlers_ofher(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)