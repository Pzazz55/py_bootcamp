'''
Python GUIs with IPyWidgets

We can build simple GUI with Jupyter - interactive elements.
This program needs to be run in Jupyter Notes only.
'''

from ipywidgets import display

def f(a, b):
    display(a + b)
    return(a + b)

w = interactive(f, a = 10, b = 20)
type(w)

w.children

display(w)