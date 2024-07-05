f = open("C:/Users/jayas/Downloads/customer1.txt", "r")


print("Q4: ")

for i in f:
    data = i.strip("\n").split(",")
    location = data[-1]
    prof = data[-2]
    if location == 'india' and prof == 'Doctor':
        print(data[1:4])