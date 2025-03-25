'''
Tuples unpacking with Python Functions
'''

# Test 1 - Write a program for tuple unpacking.
print("### Program to fetch the stock prices from a tuple - 1 ###")

stock_prices = [('APPL', 150), ('GOOG', 200), ('MSFT', 300)]
print("### Tuple Unpacking ###")
for item in stock_prices:
    print(item)

print("### Tuple Unpacking - only the ticker ###")
for ticker, price in stock_prices:
    print(price + (0.1 * price))

# Test 2 - Write a function that will return a tuple, and unpack the results from the tuple.
print("### Program to fetch the top performing employee based on most number of working hours - 2 ###")

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for work_emp, work_hrs in work_hours:
        if (work_hrs > current_max):
            current_max = work_hrs
            employee_of_month = work_emp
        else:
            pass
    return(employee_of_month, current_max)

star_emp, work_hours = employee_check([('Abby', 100), ('Billy',250), ('Cassie', 400)])
print(f'Employee of the Month is {star_emp}, with {work_hours} hours of work.')
star_employee = employee_check([('Hanuma', 100), ('Aditya',650), ('Garuda', 400)])
print(f'Employee of the Month is {star_employee[0]}, with {star_employee[1]} hours of work.')