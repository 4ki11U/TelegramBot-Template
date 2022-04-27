from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from keyboards.inline import inline_keyboards
from keyboards.reply import reply_keyboards
from aiogram import types

from conductor import dp


@dp.callback_query_handler(text=['Вперёд', 'back', 'accept_finish'])
async def kind_race_callbacks_num(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data == 'accept_finish':
        await call.answer()
        await call.message.edit_text('Отлично!')
        await call.message.answer('Что-то еще ?')
    elif call.data == 'back':
        await call.answer()
        await call.message.edit_text('Отлично!')
