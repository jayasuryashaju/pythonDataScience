def calculator(num_1, num_2, choice):
    if choice == 1:
        return num_1 + num_2
    elif choice == 2:
        return num_1 - num_2
    elif choice == 3:
        return num_1 * num_2
    elif choice == 4:
        return num_1 / num_2
    else:
        print("invalid input")


num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

print("Select a choice: \n"
      "1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n"
      ": ", end="")
choice = int(input())

print(calculator(num1, num2, choice))
