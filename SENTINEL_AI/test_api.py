import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "hour": 2,
    "location": 0,
    "device": 2
}

response = requests.post(url, json=data)

print(response.json())