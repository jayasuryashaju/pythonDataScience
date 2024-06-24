name = input("enter an identifier : ")

first_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
sub_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
flag = 0

if name[0] in first_char:
    if len(name) > 1:
        for i in range(1, len(name)):
            if name[i] not in sub_char:
                flag = 1
                break
        if flag != 1:
            print("Valid identifier")
        else:
            print("not a valid identifier")
    else:
        print("Valid identifier")
else:
    print("not a valid identifier")

