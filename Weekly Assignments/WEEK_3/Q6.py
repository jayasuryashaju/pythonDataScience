"""
Python program to check the validity of password input by users.

Min 8 letter
a capital and a small letter
and int
a special

"""


def password_validator(password):
    special_char = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    number = 0
    upper = 0
    lower = 0
    special = 0
    if len(password) >= 8:
        for i in password:
            if i.isdigit():
                number = 1
            elif i.isalpha():
                if i.isupper():
                    upper = 1
                else:
                    lower = 1
            elif i in special_char:
                special = 1

            if number == upper == lower == special == 1:
                print("valid password")
                break
        else:
            print("not valid")
    else:
        print("not valid")


# pswrd = "2ASkhg@7_jh"
pswrd = input("enter your password : ")
password_validator(pswrd)
