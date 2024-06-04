# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = int(input("enter the number of classes held : "))
classes_attended = int(input("enter the number of classes attended by the student : "))

attendance_percentage = (classes_attended / classes_held) * 100

print("attendance percentage of the student : ", round(attendance_percentage, 2))

if attendance_percentage < 75:
    print("not allowed to write exam")
else:
    print("allowed to write exam")
