import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a076f0e5a201ce570d188558e971fe11"
weather_params = {
    "lat": 28.984463,
    "lon":77.706413,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if int(condition_data) < 700:
        will_rain = True
if will_rain:
    print("bring an umbrella")

#####################################################incomplete#########################################