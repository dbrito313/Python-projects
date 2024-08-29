def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
}

calculating = True

num1 = float(input("Insert number:"))
for symbol in operations:
    print(symbol)
operator = input("Operator ('+', '-', '*', '/'):")
num2 = float(input("Insert number:"))

result = operations[operator](num1, num2)
print(result)

def additional_operation():
    num1 = result
    operator = input("Operator ('+', '-', '*', '/'):")
    new_num = float(input("Insert number:"))
    new_result = operations[operator](num1, new_num)
    print(new_result)



go_again = input("Do you wish to use previous result ? 'y' or 'n': ").lower()

while go_again == "y":
    operator = input("Operator ('+', '-', '*', '/'):")
    new_num = float(input("Insert number: "))
    result = operations[operator](result, new_num)
    print(result)
    go_again = input("Do you wish to use the previous result? 'y' or 'n': ").lower()