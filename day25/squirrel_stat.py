import pandas

data = pandas.read_csv(
    "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240425.csv"
)
gray_count = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
red_count = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
black_count = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()

new_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_count, red_count, black_count],
}
pandas.DataFrame(new_data).to_csv("./squirre_count.csv")
