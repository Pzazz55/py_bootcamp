'''
Functions -
Functions allow us to create blocks of code that can be easily executed many times, without
needing to constantly rewrite the entire block of code.

The function naming follows snake casing (Example: name_of_function)
Snake casing is all lowercases with underscore between words.

Syntax:-
def <Function_Name>():
    """
    Docstring explains Functions.
    Optional: Multiline String to describe the function.
    """

Typically, the "return" keyword is used to send back the result of the function, instead of just
printing it. "return" allows us to assign the output of the function to a new variable.

'''

# Test 1 - Functions
def name_of_function():
    print("Hello")

print("### Program to demonstrate functions - 1 ###")
name_of_function()

# Test 2 - Functions with Parameters
def name_of_function(name):
    print("Hello " +name)

print("### Program to demonstrate functions, with parameters - 2 ###")
name_of_function("Naveen")

# Test 3 - Functions with Return Variable
def add_function(num1, num2):
    return num1 + num2

print("### Program to demonstrate functions, with return variable - 3 ###")
result = add_function(5, 2)
print(result)