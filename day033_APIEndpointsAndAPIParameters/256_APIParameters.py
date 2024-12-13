import requests

LATITUDE = 12.968644
LONGITUDE = 0.128387

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(response.status_code)

print(response.json()["results"]["sunrise"])