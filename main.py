# Defines the main function that holds our calculator program
def calculator():
    # Starts an infinite loop so the calculator keeps running until the user quits.
    while True:
        # Display the menu options in the terminal.
        print("\n--- Terminal Calculator ---")
        print("Operations: +, -, *, / (or type 'exit' to quit)")

        # Asks the user to type an operator and save it in the 'op' variable.
        op = input("Choose an operation: ")

        # Checks if the user wants to close the program.
        if op == "quit":
            print("Goodbye!")
            # this 'break' function stops the while loop and ends the program.
            break

        # Verify that the user typed one of the four allowed math symbols.
        if op in ["+", "-", "*", "/"]:

            # Use a 'try' block to catch errors if the user types letters instead of numbers.
            try:
                # Asks for two numbers and converts the text inputs into decimals (floats).
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Prints a friendly warning and skips back to the start of the loop.
                print("[Error]: Please enter valid numbers.")
                continue

            # Checks which operator was chosen by the user and prints out the matching math result.
            if op == "+":
                print(f"Result: {num1 + num2}")
            elif op == "-":
                print(f"Result: {num1 - num2}")
            elif op == "*":
                print(f"Result: {num1 * num2}")
            elif op == "/":
                # Prevents the program from crashing if the second number is zero.
                if num2 == 0:
                    print("[Error]: Cannot divide by zero.")
                else:
                    print(f"Result: {num1 / num2}")

            # Handles cases of where the user typed an unsupported symbol or word.
            else:
                print("Invalid operation, Try again.")

# this function Calls the function called 'calculator' to actually start the program when the file runs.
calculator()
