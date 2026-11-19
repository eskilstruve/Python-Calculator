def calculator():
    while True:
        print("\n--- Terminal Calculator ---")
        print("Operations: +, -, *, / (or type 'exit' to quit)")

        op = input("Choose an operation: ")
        if op == "quit":
            print("Goodbye!")
            break

        if op in ["+", "-", "*", "/"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("[Error]: Please enter valid numbers.")
                continue
            
            if op == "+":
                print(f"Result: {num1 + num2}")
            elif op == "-":
                print(f"Result: {num1 - num2}")
            elif op == "*":
                print(f"Result: {num1 * num2}")
            elif op == "/":
                if num2 == 0:
                    print("[Error]: Cannot divide by zero.")
                else:
                    print(f"Result: {num1 / num2}")
            else:
                print("Invalid operation, Try again.")


calculator()
