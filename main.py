import json

import requests
pay = input("Чем платите: ").upper()
by = input("Что покупаете: ").upper()
quantity = input("Сколько отдаёте: ")

url = f"https://api.apilayer.com/exchangerates_data/convert?to={by}&from={pay}&amount={quantity}"

payload = {}
headers = {
  "apikey": "XU0CvRHu2ymn7Q3sWYv2pVmYbYSlmAyZ"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

a = json.loads(result)


print(a)