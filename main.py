import requests
import schedule
import time
import json

FILE_PATH = "./data.json"
RUN_EVERY = 15 # minutes
API_URL = "https://www.swissgrid.ch/bin/services/apicache?path=/content/swissgrid/de/home/operation/grid-data/current-data/jcr:content/parsys/livedatawidget_copy"

def format_data(json_data):
    data = json_data["data"]
    formatted_data = {
        "current": data["table"][0]["label"],
        "date": data["table"][1]["label"],
        "export-de": data["marker"][0]["text2"],
        "export-at": data["marker"][1]["text2"],
        "export-it": data["marker"][2]["text2"],
        "export-fr": data["marker"][3]["text2"]
    }
    return formatted_data

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
        save_data(format_data(data))
    else:
        print("Request failed!")
        print("With response status:", response.status_code)

schedule.every(RUN_EVERY).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
