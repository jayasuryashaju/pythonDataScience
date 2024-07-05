"""
id, name, year, rating, duration


2. 1975 < 2000 : name, rating, duration

"""

f = open("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", "r")

for i in f:
    data = i.strip('\n').split(",")
    year = data[2]
    if '1975' < year < '2000':
        print(data[1] + str(data[3:]))
