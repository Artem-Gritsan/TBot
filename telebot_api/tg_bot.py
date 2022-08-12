from aiogram import  executor
from create_bot import dp



from handlers import getWeather, start, getWiki

start.register_hadler_start(dp)
getWeather.register_handler_weather(dp)
getWiki.register_handler_wiki(dp)









if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)