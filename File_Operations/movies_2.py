"""
movie:
    id name year rating duration
"""

f = open("C:/Users/jayas/OneDrive/Documents/movies_cleaned_pandas.csv", 'r')

count = 0
movie_list = []


for i in f:
    data = i.strip("\n").split(",")

    for j in movie_list:
        print(j)
        if data[1] not in j:
            movie_list.append(data)
            print("jdbjhdsjfhbsjdhfbjhdsfjhsbf")
        else:
            print("jayasurya")

print(count)
