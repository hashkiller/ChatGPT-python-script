import requests
from bs4 import BeautifulSoup

def get_info(username: str) -> dict:
    # Récupérer la page du profil Instagram
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Récupérer les informations du profil
    data = {}
    data["username"] = username
    data["full_name"] = soup.find("h1", {"class": "rhpdm"}).text
    data["bio"] = soup.find("div", {"class": "pYkA5"}).text
    data["website"] = soup.find("a", {"class": "yLUwa"})["href"]
    data["followers"] = soup.find("span", {"class": "g47SY"}).text
    data["following"] = soup.find("span", {"class": "g47SY"}).next_sibling.next_sibling.text
    data["posts"] = soup.find("span", {"class": "g47SY"}).next_sibling.next_sibling.next_sibling.next_sibling.text

    return data

# Utilisation de la fonction
info = get_info("instagram")
print(info)