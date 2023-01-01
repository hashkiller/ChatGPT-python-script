import requests
from bs4 import BeautifulSoup

def dork_search(dork):
    # Build the search URL
    url = f'https://www.google.com/search?q={dork}'

    # Send the GET request
    response = requests.get(url)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the search results
    for h3 in soup.find_all('h3'):
        print(h3.text)

# Example usage
dork_search('price.php?aid=')