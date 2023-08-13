import requests
import json

response = requests.get('''https://api.open-meteo.com/v1/forecast?latitude=35.7219&longitude=51.3347&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m''')

res = response.json()
print(type(res))
print('temperature: ', res['hourly']['temperature_2m'][5])
print('windspeed: ', res['hourly']['windspeed_10m'][5])
print('relativehumidity', res['hourly']['relativehumidity_2m'][5])

with open('weather.json', 'w') as _f:
    json.dump(res, _f)

#_f = open('weather.json', 'w')
#json.dump(res, _f)
#_f.close()import flask

