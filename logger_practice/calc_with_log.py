import logging
from enum import Enum

# Configure the logger
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
            if choice in [1, 2, 3, 4, 5]:
                return Clac_Menu(choice)
            else:
                print("Invalid choice. Please select a valid option (1-4).")
                logging.warning("Invalid choice selected.")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            logging.error("Invalid input entered.")

def add(num1, num2):
    result = num1 + num2
    logging.info(f"Added {num1} and {num2}. Result: {result}")
    return result

def sub(num1, num2):
    result = num1 - num2
    logging.info(f"Subtracted {num2} from {num1}. Result: {result}")
    return result

def multi(num1, num2):
    result = num1 * num2
    logging.info(f"Multiplied {num1} by {num2}. Result: {result}")
    return result

def divide(num1, num2):
    try:
        result = num1 / num2
        logging.info(f"Divided {num1} by {num2}. Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted.")
        print("Error: Division by zero is not allowed.")
        return None

def Clac():
    while True:
        selected_option = menu()

        if selected_option == Clac_Menu.ADD:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = add(num1, num2)
            if result is not None:
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
            if result is not None:
                print(f"Result: {result}")

        elif selected_option == Clac_Menu.EXIT:
            print("Exiting the calculator.")
            break

if __name__ == '__main__':
    Clac()
