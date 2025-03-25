# Test 1 - Functions
def say_hello():
    print("Hello")
    print('How')
    print('Are')
    print('You')

print("### Program to demonstrate functions - 1 ###")
say_hello()

# Test 2 - Functions with Parameters
def say_hello(name):
    print(f'Hello {name}')

print("### Program to demonstrate functions, with parameters - 2 ###")
say_hello('Naveen')
#say_hello()
#throws a syntax error - TypeError: say_hello() missing 1 required positional argument: 'name'

# Test 3 - Functions with Parameters with Default Value
def func_hello(name="Default"):
    print(f'Hello {name}')

print("### Program to demonstrate functions, with default value - 3 ###")
func_hello('Naveen')
func_hello()

# Test 4 - Functions with Return Variable
def add_num(num1, num2):
    return num1 + num2

print("### Program to demonstrate functions, with return variable - 4 ###")
print(add_num(10, 20))
print(add_num('10', '20'))
print(add_num(10.20, 20.152))
print(add_num(10, 20.152))