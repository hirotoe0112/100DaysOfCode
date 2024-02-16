from calculator_art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    while n2 == 0:
        print("You can't divide by 0.")
        n2 = float(input("What's the next number?: "))
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation: ")
        while not operation_symbol in operations:
            print("Invalid operation.")
            operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type others to exit.: "
        )
        if user_choice == "y":
            num1 = answer
        elif user_choice == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Goodbye.")


calculator()
