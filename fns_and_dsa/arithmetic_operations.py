def perform_operation(num1, num2, operation):
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    operation = str(input('Enter the operation (add, subtract, multiply, divide): '))
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 == 0:
                print('Cannot be divided by zero')
            elif num2 < 0:
                print('It needs to be a positive number')
            else:
                result = num1 / num2
    return result
    print(f'Result: {result}')
perform_operation()
