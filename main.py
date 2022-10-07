import requests
import schedule
import time
import json

FILE_PATH = "./data.json"
RUN_EVERY = 1 # minutes
API_URL = "https://www.swissgrid.ch/bin/services/apicache?path=/content/swissgrid/de/home/operation/grid-data/current-data/jcr:content/parsys/livedatawidget_copy"

def save_data(data):
    json_data = []
    # Read JSON file
    with open(FILE_PATH) as fp:
        json_data = json.load(fp)

    json_data.append(data)

    with open(FILE_PATH, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Saved data successfully")

def get_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Get data successfully")
        data = response.json()
        save_data(data)
        print(data)
    else:
        print("Request failed!")
        print("With response status:", response.status_code)

schedule.every(RUN_EVERY).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
