
data = 'ABDFBCDFGHJIJHA'
dic = {}

for i in data:
    if i not in dic:
        dic[i] = 1
    else:
        print("the first recursive element is  : ", i)
        break
