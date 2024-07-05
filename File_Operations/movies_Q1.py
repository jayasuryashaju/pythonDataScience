"""
id, name, year, rating, duration


1. release year above 2000: name, year, rating

"""

f = open("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", "r")

for i in f:
    data = i.strip('\n').split(",")
    year = data[2]
    if year > '2000':
        print(data[1:4])
