def safe_divide(numerator, denominator):
    try:
        denominator = float(denominator)
        numerator = float(numerator)
        result = numerator / denominator
        return f'The result of the division is {result}'
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    except ValueError:
        return 'Error: Please enter numeric values only.'
