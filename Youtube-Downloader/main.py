import pytube

# Demande à l'utilisateur de saisir l'URL de la vidéo YouTube à télécharger
url = input("Saisissez l'URL de la vidéo YouTube à télécharger : ")

# Crée un objet Video à partir de l'URL
video = pytube.YouTube(url)

# Affiche les titres et les résolutions de toutes les versions disponibles de la vidéo
for i, stream in enumerate(video.streams):
    print(f'{i+1}. {stream.default_filename} ({stream.resolution})')

# Demande à l'utilisateur de choisir la résolution souhaitée
choice = int(input("Saisissez le numéro de la résolution souhaitée : "))

# Sélectionne la version de la vidéo correspondant à la résolution choisie
selected_stream = video.streams[choice - 1]

# Télécharge la vidéo dans le répertoire courant
selected_stream.download()

print("Téléchargement terminé !")