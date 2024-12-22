import requests

API_KEY = 'KEY'
URL = f'http://api.weatherstack.com/current?access_key={API_KEY}'

location = input('city: '), input('country: ')
querystring = {
    'query': location
}

r = requests.get(URL, params=querystring)
data = r.json()
temperature = data['current']['temperature']
Wind_Speed = data['current']['wind_speed']
Wind_Dir = data['current']['wind_dir']
Precip = data['current']['precip']
Cloudcover = data['current']['cloudcover']
Visibility = data['current']['visibility']

Full_data = {
    'City and Country':location,
    'Temperature':temperature,
    'Wind_Speed':Wind_Speed,
    'Wind_Dir':Wind_Dir,
    'Precip':Precip,
    'Cloudcover':Cloudcover,
    'Visibility':Visibility,
}

f = open('Weather_data.csv', 'w')
f.write(str(f'Weather_data:\n{Full_data}'))
