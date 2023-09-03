# Calculator Program

This is a simple command-line calculator program written in Python. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division. Users can select an operation from the menu, input two numbers, and the program will calculate and display the result.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Features

- Supports four basic arithmetic operations: addition, subtraction, multiplication, and division.
- Provides a user-friendly menu for operation selection.
- Handles invalid input gracefully and provides appropriate error messages.
- Logs operations and results to a log file for reference.

## Getting Started

To run this calculator program, you need to have Python installed on your system. If you don't have Python installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to get started:

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the `calculator.py` file is located.

3. Run the program by executing the following command:

   ```
   python calculator.py
   ```

## Usage

1. Upon running the program, you will see a menu with options to perform various operations:

   ```
   Calculator Menu:
   1. Add
   2. Subtract
   3. Multiply
   4. Divide
   5. Exit
   ```

2. Enter a number (1-5) to select the corresponding operation.

3. If you choose an arithmetic operation (Add, Subtract, Multiply, or Divide), you will be prompted to enter two numbers.

4. The program will calculate and display the result.

5. You can continue to perform operations or exit the program by selecting option 5.

## Logging

This calculator program includes logging functionality. It logs the following events:

- When an invalid choice is made in the menu.
- When invalid input is entered (e.g., a non-numeric value).
- When a division by zero is attempted.
- When arithmetic operations are performed, it logs the operation and the result.

The log messages are stored in a file named `calculator.log` in the same directory as the program.

## Contributing

If you'd like to contribute to this calculator program, please fork the repository and create a pull request. We welcome contributions, bug fixes, and improvements.

## License

This calculator program is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

---

Feel free to modify this README to include additional information or custom instructions as needed for your project.
