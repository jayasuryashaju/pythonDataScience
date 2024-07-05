

f = open("C:/Users/jayas/Downloads/temper", "r")

temperature_dict = {}

for i in f:
    data = i.strip('\n').split(',')
    if data[0] not in temperature_dict:
        temperature_dict[data[0]] = data[1]
    else:
        if data[1] > temperature_dict[data[0]]:
            temperature_dict[data[0]] = data[1]


for k,v in temperature_dict.items():
    print(k, " : ", v)