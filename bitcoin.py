import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
resp = requests.get(url)
json = resp.json()
print(json["bpi"]["EUR"]["rate"])