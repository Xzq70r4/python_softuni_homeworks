import requests
from datetime import datetime

API_KEY = '965acdac1ae64cf06761bb563ad34d96'
UNITS = 'metric' # This is for Europe measuring units, default for API is USA standard

KEY_DT = 'dt'
KEY_MAIN = 'main'
KEY_TEMP = 'temp'
KEY_PRESSURE = 'pressure'
KEY_HUMIDITY = 'humidity'
KEY_WIND = 'wind'
KEY_SPEED = 'speed'
KEY_NAME = 'name'

NO_DATA_VALUE = 'NO DATA'


def main():

    input_city = input('Input city: ')

    if input_city:
        weather_data = get_weather_data(city=input_city)

        if input_city == weather_data.get(KEY_NAME):
            city_name, dt, temp, pressure, humidity, speed = processing_data(weather_data)
            print("""
    Information for: {}
    Information to: {}
    Temperature: {} Celsius
    Pressure: {} hPa
    Humidity: {}%
    Wind: {} meter/sec
            """.format(city_name, dt, temp, pressure, humidity, speed))
        else:
            print("No information for this city!!!")
    else:
        print("You must input city!!!")


def get_weather_data(city: str, appid: str=API_KEY, units: str=UNITS):
    try:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather',
                                params={
                                    'q': city,
                                    'appid': appid,
                                    'units': units
                                    },
                                timeout=20,
                                )

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print("Error from server: ", response.status_code)
            return None

    except Exception as e:
        print("Error from server! ", str(e))


def processing_data(data):
    city_name = data.get(KEY_NAME, NO_DATA_VALUE)
    dt = data.get(KEY_DT, NO_DATA_VALUE)
    if dt:
        dt = datetime.fromtimestamp(dt)
        dt = dt.strftime('%d.%m.%Y %H:%M')

    main_data = data.get(KEY_MAIN, NO_DATA_VALUE)
    if main_data:
        temp = main_data.get(KEY_TEMP, NO_DATA_VALUE)
        pressure = main_data.get(KEY_TEMP, NO_DATA_VALUE)
        humidity = main_data.get(KEY_TEMP, NO_DATA_VALUE)
    else:
        temp = NO_DATA_VALUE
        pressure = NO_DATA_VALUE
        humidity = NO_DATA_VALUE

    wind = data.get(KEY_WIND, NO_DATA_VALUE)
    if wind:
        speed = wind.get(KEY_SPEED, NO_DATA_VALUE)
    else:
        speed = NO_DATA_VALUE

    return city_name, dt, temp, pressure, humidity, speed


if __name__ == '__main__':
    main()