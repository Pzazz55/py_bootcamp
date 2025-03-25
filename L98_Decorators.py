'''
The decorators allow you to decorate a function.
Python has decorators that allow you to tack on extra functionality to an already existing function.
They use the @ operator and are then placed on top of the original function.
'''

#Program 1: Function are objects that can be passed into other objects.
def hello():
    return "Hello !"

print("***** Program to demonstrate that the functions are objects that can be passed into other objects - Example 1 ******")
print(hello())
print(hello)

greet = hello
print(greet())

del hello
# print(hello())
# print(hello)
print(greet()) #This still returns 'Hello !'.
#Even through we deleted the name hello, the name greet is still referencing to the original function object.
#Note that, the functions are objects that can be passed into other objects.

#Program 2: Function defining another function inside it, and then returning that function.
def hello(name="Nahush"):
    print('The hello() function has been executed !')

    def greet():
        return '\t This is the greet() function inside hello!'

    def welcome():
        return '\t This is welcome() inside hello!'

    print('I am going to return a function!!')

    if name == 'Nahush':
        return greet
    else:
        return welcome

print("***** Program to demonstrate function retuning/calling another function - Example 2 ******")
my_new_func = hello('Nahush')
print(my_new_func())

#Program 3: Function defining another function inside it, and then returning that function.
def cool():
    def super_cool():
        return 'I am very cool !'

    return super_cool()

print("***** Program to demonstrate function retuning/calling another function - Example 3 ******")
some_func = cool()
print(some_func)

#Program 4: Function being passed as an Argument - pass in a function into another function and then execute the function.
def hello():
    return 'Hi Naveen !'

def other(some_def_func):
    print('Other code runs here !')
    print(some_def_func()) #this is called as passing a function.

print("***** Program to demonstrate function being passed as an Argument - Example 4 ******")
other(hello)

#Program 5a: Creating a decorator.
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, BEFORE the original function!')
        original_func()
        print('Some extra code, AFTER the original function!')
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated !!")

print("***** Program to demonstrate decorator - Example 5a ******")
# func_needs_decorator()
decorate_func = new_decorator(func_needs_decorator)
decorate_func()

#Program 5b: Creating a decorator
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, BEFORE the original function!')
        original_func()
        print('Some extra code, AFTER the original function!')
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated !!")

print("***** Program to demonstrate decorator - Example 5b ******")
func_needs_decorator()


