# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for datum in data:
#         if datum[1] != "temp":
#             temperatures.append(int(datum[1]))
#     print(temperatures)

import pandas

weather_data = pandas.read_csv("weather_data.csv")
print(weather_data)

temperature_list = weather_data["temp"].mean()
# map(int, temperature_list)
# print(sum(temperature_list) / len(temperature_list))
print(temperature_list)
print(weather_data["temp"].max())
print(weather_data[weather_data.temp == weather_data.temp.max()])

# create data frame
data_dict = {
    "students": ["Amy", "Jesse", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data_csv = data.to_csv("new_data.csv")

print(data_csv)