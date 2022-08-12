import os
from aiogram import types, Dispatcher
from create_bot import dp
import requests, datetime
from keyboards import keyboards_menu
from  aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text



class FSMWeather(StatesGroup):
    city = State()




async def weather_command(message: types.Message):
    await FSMWeather.city.set()
    await message.answer('Введите название города')

async def cansel_weather(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Ок', reply_markup=keyboards_menu.main_menu)

async def city(message: types.Message):
    get_req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={os.getenv("WEATHER_TOKEN")}&units=metric&lang=ru'
    )
    data = get_req.json()

    if len(data) == 2:
        await message.answer('Не удалось найти такой город.')
    else:
        dt = datetime.datetime.now().strftime('%H:%M')

        name_city = data['name']
        temp = round(data['main']['temp'])
        description = data['weather'][0]['description']
        wind = round(data['wind']['speed'])
        answer = (
            f'{dt}\n'
            f'Погода в городе: {name_city}\n'
            f'Температура: {temp}℃\n'
            f'Описание: {description}\n'
            f'Ветер: {wind} м/c'
        )
        await message.answer(answer, reply_markup=keyboards_menu.back_menu)



def register_handler_weather(dp: Dispatcher):
    dp.register_message_handler(weather_command, commands=['weather'], state=None)
    dp.register_message_handler(weather_command, Text(equals='Погода', ignore_case=True), state=None)
    dp.register_message_handler(cansel_weather, state=FSMWeather.city, commands='back')
    dp.register_message_handler(cansel_weather, Text(equals='Назад', ignore_case=True), state=FSMWeather.city)
    dp.register_message_handler(city, state=FSMWeather.city)
