import requests
import datetime
from config import weather_token
from pprint import pprint
def get_weather(weather_token, city):
     get_req = requests.get(
         f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric&lang=ru'
     )
     data = get_req.json()

     if len(data) == 2:
        return 'Город не найден. Проверьте название города'
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
        return answer






def main():
    city = input('Введите город: ')
    get_weather(weather_token, city)



if __name__ == '__main__':
    main()


