from config import token
from pprint import pprint
import requests
import datetime


def get_weather(city, token):
    code_to_smile = {
        'Clear': 'Clearly \U00002600',
        'Clouds': 'Cloudly \U00002601',
        'Rain': 'Rainy \U00002614',
        'Drizzle': 'Drizzly \U00002614',
        'Thunderstorm': 'Storm \U000026A1',
        'Snow': 'Snowly \U0001F328',
        'Mist': 'Mistly \U0001F328'
    }
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric'
        )
        data = r.json()
        pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'OPEN YOU EYES!!!'

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        pressure = data['main']['pressure']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        time_of_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime\
            .fromtimestamp(data['sys']['sunrise'])
        print(f'----{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}----\n'
              f'Сity: {city}\n'
              f'Temp: {cur_weather} °C {wd}\n'
              f'Humidity: {humidity} %\n'
              f'Wind: {wind} м/c\n'
              f'Pressure: {pressure} мм рт. ст.\n'
              f'Sunrise: {sunrise_timestamp}\n'
              f'Sunset: {sunset_timestamp}\n'
              f'Daylong: {time_of_day}')
    except Exception as ex:
        print(ex)
        print('Error!')


def main():
    city = input('Set city: ')
    get_weather(city, token)


if __name__ == '__main__':
    main()
