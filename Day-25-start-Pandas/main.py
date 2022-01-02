### TOO COMPLEX
# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temparatures = []
#     for row in data:
#         temparatures.append(row[1])
        
#     temparatures = [int(temp) for temp in temparatures[1:]]
#     print(temparatures)

## MUCH EASIER WHEN WORKING WITH CSV
# import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list) / len(temp_list))

# print("Average temp = {}".format(data["temp"].mean()))
# print("Max temp = {}".format(data["temp"].max()))

# # Get Data from column
# print(data["condition"])
# print(data.condition)

# Get Data from row
# mondays = data[data.day == "Monday"]
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])



# data_dict = {
#     "Names": ["Leo", "John", "Thinh"],
#     "Scores": [50, 60, 70]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

######## Squirrel Data #########
import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Primary Fur Color": ["Gray", "Black", "Cinnamon"],
    "count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

pd.DataFrame(data_dict).to_csv("exported_Squirrel.csv")

print(len(data))