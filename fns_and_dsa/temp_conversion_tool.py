global FARENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FARENHEIT_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def main():
    temp = float(input('Enter the temperature to convert: '))
    unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()
    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f'{temp}°C is {converted_temp:.2f}°F')
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f'{temp}°F is {converted_temp:.2f}°C')
    else:
        print('Invalid unit, Enter C for celsius or F for fahrenheit')
main()
