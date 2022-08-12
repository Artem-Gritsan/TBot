from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain= KeyboardButton('Главное меню')

btn_weather = KeyboardButton('Погода')
btnWiki = KeyboardButton('Википедия')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_weather, btnWiki)

btnBack = KeyboardButton('Назад')
back_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBack)