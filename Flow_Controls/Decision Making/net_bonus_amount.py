# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


salary = int(input("enter your salary : "))
experience = int(input("enter your experience(in years) : "))

if experience > 5:
    bonus = salary * .05  #(salary * (5/100))
    print("bonus amount is = ", bonus)
else:
    print("no bonus available")
