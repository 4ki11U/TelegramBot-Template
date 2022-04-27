from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
import re

back_inline_bt = InlineKeyboardButton('🔙 Назад', callback_data='back')
accept_inline_bt = InlineKeyboardButton('☑️ Подтвердить', callback_data='accept_finish')

accept_back_keybd = InlineKeyboardMarkup(row_width=1).add(accept_inline_bt, back_inline_bt)


def main_kb_from_db():
    from_db = select()

    my_list_for_buttons = []
    for race in from_db:
        clear_result = re.sub(r"[(',)]", "", str(race))
        my_list_for_buttons.append(clear_result)

    button_list = [types.InlineKeyboardButton(text=name, callback_data=name) for name in my_list_for_buttons]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*button_list)

    return keyboard
