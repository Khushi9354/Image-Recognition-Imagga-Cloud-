import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url": "https://static.toiimg.com/photo/msid-50301278,width-96,height-65.cms"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzc2YTBkYzVhZDA5MDVjYzo2ODZjMmI1NThhNTc0N2E1NTFiNTc3OGIxOTMxNWViOA=="
    }

response = requests.request("GET",url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
