import requests
import sleep

url = "http://www.google.com.tw"

with requests.get(url, timeout=30) as res:
    print(res.status_code)

time.sleep(1)