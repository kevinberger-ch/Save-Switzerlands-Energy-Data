import requests

API_URL = "https://www.swissgrid.ch/bin/services/apicache?path=/content/swissgrid/de/home/operation/grid-data/current-data/jcr:content/parsys/livedatawidget_copy"

response = requests.get(API_URL)
if response.status_code == 200:
    print("Get data successfully")
    data = response.json()
    print(data)
else:
    print("Request failed!")
    print("With response status:", response.status_code)
