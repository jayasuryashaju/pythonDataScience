side_1 = int(input("enter length of side one : "))
side_2 = int(input("enter length of side two : "))
side_3 = int(input("enter length of side three : "))

if side_1 != side_2 != side_3:
    print("Scalene")
elif side_1 == side_2 == side_3:
    print("Equilateral")
elif side_2 == side_1 or side_3 == side_1 or side_2 == side_3:
    print("Isosceles")
else:
    print("not a triangle")
    