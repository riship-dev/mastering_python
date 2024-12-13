import json

# Data to write to a JSON file
data = {
    "name": "Rishi",
    "age": 21,
    "skills": ["Python", "JavaScript", "SQL"]
}

# Writing JSON data to a file using json.dump()
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
    print("Data written to file.")

# Reading JSON data from a file using json.load()
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("\nLoaded Data:", loaded_data)

# Updating JSON data
loaded_data["skills"].append("React")
loaded_data["city"] = "Chennai"

# Writing updated data back to the file
with open("data.json", "w") as file:
    json.dump(loaded_data, file, indent=4)
    print("\nData updated and written to file.")