# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours
# worked above 40 hours. Put the logic to do the computation of pay in a function called computepay()
# and use the function to do the computation. The function should return a value. Use 45 hours and
# a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read
# a string and float() to convert the string to a number. Do not worry about error checking the user input
# unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

hours = input("Enter Hours:")
rate = input("Enter the rate:")


def rate_validation(rate):
    try:
        rate = float(rate)
    except:
        print('Enter the number')
    if rate < 0:
        print('Enter a positive number')
    elif rate == 0:
        print('Are you working for free?')
    return float(rate)


def calculate_pay(hours, salary):
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * rate * 1.5
    return salary


def hours_validation(hours):
    try:
        hours = float(hours)
    except:
        print('Enter the number')
    hours = float(hours)
    if hours < 0:
        print('Enter a positive number')
    elif hours == 0:
        print('Are you working at all?')
    elif hours > 750:
        print('There are 750 hours in the month only')
    return hours


rate = rate_validation(rate)
hours = hours_validation(hours)
salary = calculate_pay(hours, rate)
print("Pay", salary)
