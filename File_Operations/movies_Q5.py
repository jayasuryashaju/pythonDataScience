"""
5. each year movie count

"""

f = open("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", "r")

movie_count_dict = {}

for i in f:
    data = i.strip("\n").split(",")
    if data[-3] not in movie_count_dict:
        movie_count_dict[data[-3]] = 1
    else:
        movie_count_dict[data[-3]] += 1

for k, v in movie_count_dict.items():
    print(k, " : ", v)
