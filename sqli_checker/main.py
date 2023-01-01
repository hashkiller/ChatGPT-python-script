import requests
from bs4 import BeautifulSoup

def sqli_check(url, payload):
    # Send the GET request with the payload
    response = requests.get(url, params={'id': payload})

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the payload is present in the response
    if payload in soup.text:
        print('Vulnerability found!')
    else:
        print('No vulnerability found.')

# Example usage
sqli_check('http://example.com/getuser.php', '1 OR 1=1')