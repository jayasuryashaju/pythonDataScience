"""
movie:
    id name year rating duration
"""

f = open("C:/Users/jayas/OneDrive/Documents/movies_cleaned_pandas.csv", 'r')

count = 0

for i in f:
    count += 1
print("row count : ", count)