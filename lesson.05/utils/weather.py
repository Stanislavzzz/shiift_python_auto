import requests
from config import TOKEN_WEATHER


def get_weather(our_city):
    api_key = TOKEN_WEATHER
    lang = "ru"
    city = our_city

    # url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&lang={lang}&units=metric'
    # response = requests.get(url)

    url = f'https://api.openweathermap.org/data/2.5/weather'

    params = {
        "q": city,
        "appid": api_key,
        "lang": lang,
        "units": "metric"
    }

    response = requests.get(url, params=params)


    if response.status_code == 200:
        result = response.json().get("main").get("temp")
        return result

    else:
        return None


if __name__ == '__main__':
    print(get_weather("Сочи"))