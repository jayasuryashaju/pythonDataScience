"""
GRADING SYSTEM
"""
mark = int(input("Enter your mark : "))
grade = ""
if mark >= 80:
    grade = "A"
elif 60 <= mark < 80:
    grade = "B"
elif 50 <= mark < 60:
    grade = "C"
elif 45 <= mark < 50:
    grade = "D"
elif 25 <= mark < 45:
    grade = "E"
elif mark < 25:
    grade = "F"

print(grade)
