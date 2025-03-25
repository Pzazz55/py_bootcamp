'''
Python GUIs with IPyWidgets

We can build simple GUI with Jupyter - interactive elements.
This program needs to be run in Jupyter Notes only.
'''

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

#at a basic level the interact function will auto generate the user interface control for some sort of 
#function argument, and it calles the function with those arguments and allows to manipulate interactively.

######### SNIPPET - 1 #########
def func(x):
    return x

interact(func, x = 10) #this creates an interactive slider  (on passing Integer value)
interact(func, x = True) #this creates an interactive checkbox (on passing Boolean Value)
interact(func, x = 'Hello') #this creates an interactive textbox (on passing String Value)
interact(func, x = ['Option1', 'Option2', 'Option3']) #this creates an interactive dropdown (on passing a list of strings)
interact(func, x = {'one':10, 'two':20}) #this creates an interactive dropdown (on passing a dictionary of values)

######### SNIPPET - 2 #########
def func(x):
    return x

interact(func, x = fixed('Hello')) #this creates a fixed textbox and no more interactive

######### SNIPPET - 3 #########
@interact (x=True, y=1.0) #a decorator
def g(x, y):
    return (x, y) #a simple function to return a tuple of x and y

######### SNIPPET - 4 #########
@interact (x=True, y=fixed(1.0)) #the value of 'y' is fixed and no more interactive.
def g(x, y):
    return (x, y) #a simple function to return a tuple of x and y


######### SNIPPET - 5 #########
def func(x):
    return x

interact(func, x = 10) #the minimum is defined by 'x' and the maximum is defined by 'x times 3'
#inorder to change the mix and max, we need to use 'Abbreviation of the Widget'
interact(func, x = widgets.IntSlider(min=-100, max=100, step=1, value=0)) #Approach 1
interact(func, x=(-100, 100, 1)) #Approach 2
#the min value is -100, the max value is 100, the step size is 1, and the starting value is 0

#to change the above to floating point
interact(func, x=(-10.0, 10.0, 0.1))

#achiving the above using a interact decorator
@interact (x=(0.0, 20.0, 0.5))
def h(x=5.0):
    return(x)



