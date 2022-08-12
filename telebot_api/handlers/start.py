from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import keyboards_menu




# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=keyboards_menu.main_menu)




def register_hadler_start(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    # dp.register_message_handler(something)


