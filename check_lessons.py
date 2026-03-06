import json
import requests

url = "https://dog.ceo/api/breed/hound/images"
result = requests.get(url)
result_list = list(result.json()["message"])
count = 0
for i in result_list:
    if "hound-english" in i:
        count += 1
print(count)