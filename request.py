import requests
import xml.etree.ElementTree as ET

from K import K

keyManager = K()
key = keyManager.getKey()

urlFront = "https://apis.data.go.kr/B090041/openapi/service/LrsrCldInfoService/getLunCalInfo?"
testUrlQuery = "solYear=2023&solMonth=04&solDay=&ServiceKey=" + key
url = urlFront + testUrlQuery

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML data using ElementTree
    root = ET.fromstring(response.content)
    
    # Find a lunar day
    body = root.find(".//body")
    items = body.find(".//items")
    item = body.find(".//item")
    lunDay = item.find('.//lunDay')

    print(lunDay.text)


else:
    # If the request was not successful, print an error message
    print('Error:', response.status_code)