def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    operation = 'add','subtract','multiply', 'divide'
    match operation:
        case 'add':
            add = num1 + num2
        case 'subtract':
            subtract = num1 - num2
        case 'multiply':
            multiply = num1 * num2
        case 'divide':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                divide = num1 / num2
        case _:
            print("Enter number.")
    return add, subtract, multiply, divide