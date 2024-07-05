
f = open("C:/Users/jayas/Downloads/sample4.txt", "r")

lst = []

# for i in f:
#     data = i.strip("\n").split(",")
#     if data[3] > '23':
#         print(data[1:5])
#     lst.append(data)


# for i in f:
#     data = i.strip("\n").split(",")
#     if data[3] == '22':
#         print(data[1::2])
#     lst.append(data)

# for i in f:
#     data = i.strip("\n").split(",")
#     location = data[-1]
#     if location == 'Chennai':
#         print(data[1:5])
#     lst.append(data)


for i in f:
    data = i.strip("\n").split(",")
    location = data[-1]
    age = data[3]
    if location == 'Chennai' and age > '23':
        print(data[1:])
    lst.append(data)