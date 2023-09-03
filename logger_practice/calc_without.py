import logging
from enum import Enum


class Clac_Menu(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    EXIT = 5

def menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Select an option (1-5): "))
            if choice in [1, 2, 3, 4 ,5]:
                return Clac_Menu(choice)
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

def Clac():
    while True:
        selected_option = menu()

        if selected_option == Clac_Menu.ADD:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = add(num1, num2)
            print(f"Result: {result}")

        elif selected_option == Clac_Menu.SUBTRACT:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = sub(num1, num2)
            print(f"Result: {result}")

        elif selected_option == Clac_Menu.MULTIPLY:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = multi(num1, num2)
            print(f"Result: {result}")

        elif selected_option == Clac_Menu.DIVIDE:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = divide(num1, num2)
            print(f"Result: {result}")

        elif selected_option == Clac_Menu.EXIT:
            print("Exiting the calculator.")
            break

if __name__ == '__main__':
    Clac()
