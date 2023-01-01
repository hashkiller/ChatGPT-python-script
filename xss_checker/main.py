import requests
from bs4 import BeautifulSoup

def xss_check(url, payload):
    # Send the GET request with the payload
    response = requests.get(url, params={'input': payload})

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the payload is present in the response
    if payload in soup.text:
        print('Vulnerability found!')
    else:
        print('No vulnerability found.')

# Example usage
xss_check('http://example.com/search.php', '<script>alert("XSS")</script>')