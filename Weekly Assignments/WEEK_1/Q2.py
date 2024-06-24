idf = "name age 94js $%hvu 2k Apple 4899"
x = idf.split(" ")
new_lst = []
for name in x:
    if name.isidentifier():
        new_lst.append(name)
print(x)
print(new_lst)
