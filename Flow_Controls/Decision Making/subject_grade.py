mark_sub1 = int(input("enter the mark of subject ONE : "))
mark_sub2 = int(input("enter the mark of subject TWO : "))
mark_sub3 = int(input("enter the mark of subject THREE : "))
mark_sub4 = int(input("enter the mark of subject FOUR : "))

total_marks = mark_sub1 + mark_sub2 + mark_sub3 + mark_sub4

print("total marks : ", total_marks)

if total_marks >= 180:
    print("grade : A+")
elif 160 <= total_marks <= 179:
    print("grade : A")
elif 140 <= total_marks <= 159:
    print("grade : B+")
elif 120 <= total_marks <= 139:
    print("grade : B")
elif 100 <= total_marks <= 119:
    print("grade : C+")
elif 80 <= total_marks <= 99:
    print("grade : C")
else:
    print("Failed")
    