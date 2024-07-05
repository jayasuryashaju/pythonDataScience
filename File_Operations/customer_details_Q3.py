f = open("C:/Users/jayas/Downloads/customer1.txt", "r")


print("Q3: ")

for i in f:
    data = i.strip("\n").split(",")
    prof = data[-2]
    if prof == 'Doctor':
        print(data[1:4])

