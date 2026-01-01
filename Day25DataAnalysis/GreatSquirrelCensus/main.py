# get only fur color data from squirrel data and count them then store it in a new csv file
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_Data.csv")

with open('squirrel_count.csv', mode='w') as file:
    file.write("Fur Color,Count\n")
    fur_color_counts = data["Primary Fur Color"].value_counts()
    for color, count in fur_color_counts.items():
        file.write(f"{color},{count}\n")

