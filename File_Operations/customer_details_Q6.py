

f = open("C:/Users/jayas/Downloads/customer1.txt", "r")

print("Q6: ")

location_dict = {}

for i in f:
    data = i.strip("\n").split(",")

    location = data[-1]

    if location not in location_dict:
        location_dict[location] = 1
    else:
        location_dict[location] += 1
for k, v in location_dict.items():
    print(k, " : ", v)
