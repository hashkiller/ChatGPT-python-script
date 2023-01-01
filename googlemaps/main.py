import googlemaps

# Entrez votre clé API Google Maps
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Saisissez les adresses de départ et d'arrivée
origin = input("Saisissez l'adresse de départ : ")
destination = input("Saisissez l'adresse d'arrivée : ")

# Obtient l'itinéraire entre les deux adresses
route = gmaps.directions(origin, destination)

# Affiche les étapes de l'itinéraire
for step in route[0]['legs'][0]['steps']:
    print(step['html_instructions'])