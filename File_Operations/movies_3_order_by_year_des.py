"""
movie:
    id name year rating duration
"""

f = open("C:/Users/jayas/OneDrive/Documents/movies_cleaned_pandas.csv", 'r')


movie_list = []


for i in f:
    data = i.strip("\n").split(",")
    movie_list.append(data)
print(movie_list)
movie_list.sort()