while True:

    print("\n===== SIMPLE CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            continue

        result = num1 / num2

    else:
        print("Invalid operation!")
        continue

    print(f"Result = {result}")

    choice = input("Do another calculation? (y/n): ")

    if choice.lower() != "y":
        print("Goodbye!")
        break