print("Welcome to the Basic calculator! \n Choose an operation: \n + for Addition \n - for Subtraction \n * for Multiplication \n / for Division")
operators = ["+", "-", "*", "/"]


calculate = True

while calculate:
    operator = input("Enter operation:")

    if operator not in operators:
        print("Please type a valid operator +, -, * or /")
        continue

    try:
        first_number = int(input('Enter number:'))
        second_number = int(input('Enter number:'))
    except ValueError:
        print("Invalid input. Please type valid numbers.")
        continue

    if operator == "+":
        result = first_number + second_number
        print(f"Result: {first_number} + {second_number} = {result}")
    elif operator == "-":
        result = first_number - second_number
        print(f"Result: {first_number} - {second_number} = {result}")
    elif operator == "*":
        result = first_number * second_number
        print(f"Result: {first_number} * {second_number} = {result}")
    elif operator == "/":
        if second_number == 0:
            print("Error! Division by zero.")
        else:
            result = first_number / second_number
            print(f"Result: {first_number} / {second_number} = {result}")
    else:
        print("Please type a valid operator +, -, * or /")
    new_calc = input('Do you want to perform another operation? "yes" or "no".').lower()
    if new_calc == "no":
        calculate = False


print("Goodbye!")

