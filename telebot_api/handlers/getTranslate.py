
from pprint import pprint
from aiogram import types, Dispatcher
from create_bot import dp
import requests
from keyboards import keyboards_menu
from  aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text


class FSMTranslate(StatesGroup):
    fromLang = State()
    toLang = State()
    text = State()

async def translate_command(message: types.Message):
    await FSMTranslate.fromLang.set()
    await message.answer('С какого языка желаете перевести текст?(Например: Английский)')
def translate(text, from_lang, to_lang):
	url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

	payload = f"q={text}&target={to_lang}&source={from_lang}"
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": "bddcbb6ad6msh7d06541660cd29ep1d2f0djsn5b8fca4c5676",
		"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
	}

	response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
	result = response.json()
	if result['data']['translations'][0]['translatedText'] == text:
		return 'Неверные параметры языка'
	return result['data']['translations'][0]['translatedText']



pprint(translate('Jesteś głupcem', 'ru', 'en'))