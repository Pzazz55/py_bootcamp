
'''
Using Arbitrary number of Arguments & Keyword Arguments in Python.
*args (Arguments) - return back a tuple
**kwargs (Keyword Arguments) - return back a dictionary

Python support Arbitrary number of Keyword Arguments - using **kwargs.
Keyword Arguments is a built-in dictionary of key, value pairs.
'''

# Test 1 -  simple function with return value
print("### Program to return 5% of the Sum of a & b - 1 ###")
def myfunc(a, b):
    #Return 5% of the sum of a & b.
    return sum((a,b)) * 0.05 #Observe here that both a and b are passed as tuples.
calc = myfunc(40, 60)
#Positional Arguments - 40 is assigned to a (because 40 is the first argument or is in the first position)
#and 60 is assigned to b (because 60 is the second argument or is in the second position)
print(calc)

# Test 2 -  Arguments in Python
print("### Program to return 5% of the sum based on number of parameters passed in the function - 2 ###")
def myfunc(a, b, c = 0, d = 0, e = 100):
    #if c, d, e values are not passed in the function call then it will take default values as mentioned
    #i.e. c = 0, d = 0, e = 100
    #Return 5% of the sum of a & b.
    return sum((a, b, c, d, e)) * 0.05
calc = myfunc(40, 60)
#Positional Arguments - 40 is assigned to a (because 40 is the first argument or is in the first position)
#and 60 is assigned to b (because 60 is the second argument or is in the second position)
print(calc)

# Test 3a -  Arguments in Python - passing Arbitrary Number of Values
print("### Program to return 5% of the sum based on arbitrary number of parameters passed in the function, using *args - 3a ###")
def myfunc(*args):
    #treat this as a tuple of parameters that are coming in.
    #Note: We can use any word instead of 'args'.
    print(args)
    return sum(args) * 0.05
calc = myfunc(40, 60, 100, 0, 200)
#Positional Arguments - 40 is assigned to a (because 40 is the first argument or is in the first position)
#and 60 is assigned to b (because 60 is the second argument or is in the second position)
print(calc)

# Test 3b -  Arguments in Python - passing Arbitrary Number of Values
print("### Program to return 5% of the sum based on arbitrary number of parameters passed into a function, using *args - 3b ###")
def myfunc(*param):
    add_items = 0
    print('The value in the tuple are: ')
    for items in param:
        print(items)
        add_items += items
    return add_items * 0.05

calc = myfunc(40, 60, 100, 0, 200)
print(f'The value returned by the function is {calc}')

# Test 4 -  Keywords in Python - passing Arbitrary Number of Values
print("### Program to illustrate arbitrary number of keyword passed into a function, using **kwargs - 4 ###")
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here.')

myfunc(fruit = 'Apple')
myfunc(fruit = 'Apple', veggie = 'lettuce')

# Test 5 -  Using Keywords and Arguments in Combination
print("### Program to illustrate arbitrary number of arguments & keyword passed into a function, using both *args & **kwargs - 5 ###")
def myfunc(*args, **kwargs):
    print('I would like {} {}'. format(args[0], kwargs['food']))

myfunc(10, 20, 30, fruite = 'Orange', food = 'Panner', animal = 'Dog')