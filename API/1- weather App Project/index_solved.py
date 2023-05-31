import requests
import json
api_key = '69faef5a3baa275f5a8448c77f9ddc50_suhail'
city = 'New York'
units = 'imperial'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}'
response = requests.get(api_url)
print(response.json())
if response.status_code==200:
    json_data=json.loads(response.text)
    main=json_data["main"]
    weather=json_data["weather"]
    weather_dict=weather[0]
    temperature=main["temp"]
    humidity=main["humidity"]
    description=weather_dict["description"]
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Description: {description}")
else:
    print("api response error")
