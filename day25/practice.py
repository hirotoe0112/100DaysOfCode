"""
with open("./weather_data.csv", mode="r") as weather_data_file:
    data = weather_data_file.read().splitlines()
    print(data)
"""

"""
import csv

with open("./weather_data.csv", mode="r") as weather_data_file:
    data = csv.DictReader(weather_data_file)
    temperatures = []
    for row in data:
        temperatures.append(int(row["temp"]))
    print(temperatures)
"""

import pandas

data = pandas.read_csv("./weather_data.csv")
temp = data["temp"]
print(type(data))
print(temp)
print(data.to_dict())
print(data.to_dict()["day"])
print(data.to_dict()["day"][0])
temp_list = temp.to_list()
print(temp_list)
sum = sum(temp_list)
print(sum / len(temp_list))
print(temp.mean())
print(temp.max())
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 1.8 + 32)

data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("./data_frame_to_csv.csv", index_label="id")
