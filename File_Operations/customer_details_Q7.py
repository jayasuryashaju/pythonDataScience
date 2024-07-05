f = open("C:/Users/jayas/Downloads/customer1.txt", "r")

print("Q7: ")

prof_dict = {}
for i in f:
    data = i.strip("\n").split(",")
    prof = data[-2]
    if prof not in prof_dict:
        prof_dict[prof] = 1
    else:
        prof_dict[prof] += 1
for k, v in prof_dict.items():
    print(k, " : ", v)
