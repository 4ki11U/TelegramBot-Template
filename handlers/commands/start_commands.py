from keyboards.reply import reply_keyboards
from aiogram import types

from conductor import bot, dp

from datetime import datetime
from database_files.Telegram_DataUsers import select_from_db, insert_into_db


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.message):
    if message.text == '/start':
        select_from_sql = select_from_db(message.from_user.id)
        if not select_from_sql:
            now = str(datetime.today().strftime('%d-%m-%Y'))
            print('в бд не найден, делаю инсерт')
            insert_into_db(message.from_user.id,
                           message.from_user.first_name,
                           message.from_user.username,
                           message.from_user.last_name,
                           now)
        await bot.send_message(message.from_user.id,
                               f"Приветствую тебя, <b>{message.from_user.first_name}</b> ,"
                               f"в моём уютненьком чатике",
                               reply_markup=reply_keyboards.start_main_menu_kb)
    elif message.text == '/help':
        await message.reply('Возникли вопросы ?\nПиши создателю бота ▶ @kpakhotin')
