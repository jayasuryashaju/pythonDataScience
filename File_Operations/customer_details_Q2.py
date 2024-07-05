f = open("C:/Users/jayas/Downloads/customer1.txt", "r")


print("Q2: ")

for i in f:
    data = i.strip("\n").split(",")
    age = data[3]
    if age > '50':
        print(data[1:5])