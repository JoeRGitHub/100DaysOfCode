# 01 method

# data = open("weather_data.csv").read()
# print(data.split(","))

# Second method

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# 03 method

# import csv
#
# with open("weather_data.csv") as data_file:
#     reader = csv.reader(data_file)
#     temperatures = []
#     # next(data_file) # can be used to skip line one
#     for row in reader:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 04 method

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# temp_dict = data.to_dict()
# print(temp_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avr = data["temp"].mean()
# print(f"Average of the list: {avr}")
#
# max = data["temp"].max()
# print(f"Maximum value of the list: {max}")
#
# condition = data["condition"]
# # print(condition)
# print(data.condition)
# #
#
# # Python program to get average of a list
# def Average(lst):
#     return sum(lst) / len(lst)
# # Driver Code
# lst = [15, 9, 55, 41, 35, 20, 62, 49]
# average = Average(temp_list)
# # Printing average of the list
# print("Average of the list =", round(average,3))

# Get the row with MAX value
# print(data[data.temp == data.temp.max()])

# Convert temp from Celsius to Fahrenheit

# monday = data[data.day == "Monday"]
# monday_cov = monday.temp[0]
# print(f"Temp in C: {monday_cov}")
#
# fahrenheit = (monday_cov * 1.8) + 32
# print(f"Temp in F: {fahrenheit}")

# Create a new DataFame from scratch

# dict = {
#     "student": ["Amy", "Bob", "Charlie", "David"],
#     "score": [60, 70, 80, 90]
#     }
#
# data_dict = pandas.DataFrame(dict)
# print(data_dict)
# data_dict.to_csv("student_data.csv")

# Count fur colors

data = pandas.read_csv("squirrel_data.csv")


fur_color = data["Primary Fur Color"]

# Old solution:

# gray = 0
# cinnamon = 0
# black = 0
# blank = 0
# for i in fur_color:
#     if i == "Gray":
#         gray += 1
#     elif i == "Cinnamon":
#         cinnamon += 1
#     elif i == "Black":
#         black += 1
#     else:
#         blank += 1
#
# print(f"Gray: {gray}\nCinnamon: {cinnamon}\nBlack: {black}\nBlank: {blank}")
#
# print(fur_color)

# Creating table from dictionary using Pandas
gray_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])
print(f"Fur Gray cont: {gray_color}\nFur Cinnamon cont: {cinnamon_color}\nFur Black cont: {black_color}")

data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Fur Cunt": [gray_color, cinnamon_color, black_color]
}
print(data_dict)

fur_data_frame = pandas.DataFrame(data_dict)
print(f"Create a table from a dict:\n {fur_data_frame}")
fur_data_frame.to_csv("fur_data_frame.csv")





