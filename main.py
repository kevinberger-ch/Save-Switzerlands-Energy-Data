import requests
import schedule
import time

RUN_EVERY = 15 # minutes
API_URL = "https://www.swissgrid.ch/bin/services/apicache?path=/content/swissgrid/de/home/operation/grid-data/current-data/jcr:content/parsys/livedatawidget_copy"

def getData():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Get data successfully")
        data = response.json()
        print(data)
    else:
        print("Request failed!")
        print("With response status:", response.status_code)

schedule.every(RUN_EVERY).minutes.do(getData)

while True:
    schedule.run_pending()
    time.sleep(1)
