
f = open("C:/Users/jayas/Downloads/customer1.txt", "r")


print("Q5: ")

for i in f:
    data = i.strip("\n").split(",")
    location = data[-1]
    age = data[3]
    if location == 'uk' and age > '55':
        print(data[1:5])