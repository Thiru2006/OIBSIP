import requests

city = input("Enter a city name to see its weather: ")
api_key = "" #Use your API Key
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"
try:
    response = requests.get(url)
    weather = response.json()
    if weather["cod"] == 200:
        print("\nWeather in", weather["name"])
        print("Temperature:", weather["main"]["temp"], "°C")
        print("Humidity:", weather["main"]["humidity"], "%")
        print("Description:", weather["weather"][0]["description"])
    else:
        print("Sorry, city not found. Please try again.")
except Exception:
    print("Oops! Something went wrong. Please check your internet or try again.")
