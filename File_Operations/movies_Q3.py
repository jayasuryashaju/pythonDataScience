"""
id, name, year, rating, duration


3. rating > 4 : name, year, rating

"""

f = open("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", "r")

for i in f:
    data = i.strip('\n').split(",")
    rating = data[-2]
    if rating > '4':
        print(data[1:4])
