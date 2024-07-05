"""
id, name, year, rating, duration


4. rating > 4 and year > 2005 : name, year, duration

"""

f = open("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", "r")

for i in f:
    data = i.strip('\n').split(",")
    rating = data[-2]
    year = data[2]
    if rating > '4' and year > '2005':
        print(data[1:4])