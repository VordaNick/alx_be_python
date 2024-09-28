from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print('Current Date: ', current_date)
    return current_date
number_of_days = int(input('Enter the number of days to add to the current date: '))
def calculate_future_date(current_date, number_of_days):
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    print('Future Date: ', formatted_future_date)
current_date = display_current_datetime()
calculate_future_date(current_date, number_of_days)