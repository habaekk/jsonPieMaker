import requests
import xml.etree.ElementTree as ET

from K import K

def request(url):

    # Make a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML data using ElementTree
        root = ET.fromstring(response.content)
        return root

    else:
        # If the request was not successful, print an error message
        print('Error:', response.status_code)
        return -1