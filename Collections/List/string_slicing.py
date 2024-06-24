string = "luminarTECHNOLAB"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

new_lst = []

for i in string:
    if i in vowels:
        new_lst.append(i)

print(new_lst)