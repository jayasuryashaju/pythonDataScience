f = open('sample2', 'r')

word_count = {}

for i in f:
    data = i.rstrip("\n").split(" ")

    for j in data:
        if j not in word_count:
            word_count[j] = 1
        else:
            word_count[j] += 1

for k, v in word_count.items():
    print(k, " : ", v)

