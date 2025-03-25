'''
The variable names that are assigned are stored in a Namespace.
The variable names also have a scope. Scope means the visibility of the variable name to
other parts of the code.

LEGB Rules (the order in which Python checks for the Variables)
----------------------------------------------------------
L: Local - Names assigned in any way within a function (def or lambda), and not declared
global in that function.
E: Enclosing Function Locals - Names in the local scope of any and all enclosing functions
(def or lambda), from inner to outer.
G: Global (Module) - Names assigned at the top-level of a module file, or declared global
in a def within the file.
B: Built-In (Module) - Names preassigned in the built-in names module: open, range,
syntaxerror, str, etc. (built-in keywords)

'''

#Program 1
print("****** Example of a Local Variable ******")
squ = lambda num: num ** 2 #num is a Local Variable.
print(squ(2))

#Program 2
print("****** Example of a Enclosing Functional Local Variable ******")
#This is a Global Variable
name = 'THIS IS A GLOBAL STRING'

def greet():
    #This is an Enclosing Function Variable
    name = 'SAMMY'

    def hello():
        name = 'THIS IS A LOCAL STRING'
        print("Hello " +name)

    hello()

greet()

# Program 3a
print("****** Example of a Enclosing Functional Local Variable ******")
# This is a Global Variable
x = 50
def func(x):
    print(f'The value of x in the functional : {x}')

    #LOCAL REASSIGNMENT !
    x = 200
    print(f'The value of x in the functional (after changing locally): {x}')

print(f'The value of x before variable reassignment : {x}')
func(x)
print(f'The value of x outside the function is : {x}') #x will be 50 and not 200

# Program 3b
print("****** Example of a Enclosing Functional Local Variable ******")
# This is a Global Variable
x = 50
def func():
    global x
    print(f'The value of x in the functional (as global variable): {x}')

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'The value of x in the functional (after changing locally): {x}')

print(f'The value of x before variable reassignment : {x}')
func()
print(f'The value of x outside the function is : {x}')