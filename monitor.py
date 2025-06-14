import time
import requests

URL = "https://google.com"
CHECK_INTERVAL = 30

while True:
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"{time.ctime()}: {URL} is UP")
        else:
            print(f"{time.ctime()}: {URL} might be DOWN. Status Code: {response.status_code}")
    except requests.ConnectionError:
        print(f"{time.ctime()}: {URL} is DOWN. Failed to connect.")
    time.sleep(CHECK_INTERVAL)

