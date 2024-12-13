import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json())

iss_information = response.json()
latitude = iss_information["iss_position"]["latitude"]
longitude = iss_information["iss_position"]["longitude"]
print(f"{latitude} {longitude}")