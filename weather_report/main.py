import requests

# Entrez votre clé API OpenWeatherMap
api_key = 'YOUR_API_KEY'

# Saisissez l'emplacement pour lequel vous souhaitez obtenir la météo
location = input("Saisissez l'emplacement pour lequel vous souhaitez obtenir la météo : ")

# Envoie une requête à l'API OpenWeatherMap pour obtenir les données météorologiques de l'emplacement
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')

# Charge les données météorologiques sous forme de dictionnaire Python
weather_data = response.json()

# Affiche la température actuelle
temperature = weather_data['main']['temp']
print(f'La température actuelle à {location} est de {temperature}°C.')

# Affiche le résumé de la météo
description = weather_data['weather'][0]['description']
print(f'Le temps est actuellement : {description}.')