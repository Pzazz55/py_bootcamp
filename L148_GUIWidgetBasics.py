'''
GUI Widget Basics
This program needs to be run in Jupyter Notes only.
!pip install ipywidgets
'''
import ipywidgets as widgets
w = widgets.IntSlider()

from IPython.display import display
display(w)

display(w)

w.close() #to close a widget

#Widgets also have properties
w = widgets.IntSlider()
display(w)
w.value
w.value = 50
w.keys
w.max = 2000

#Connecting/Linking two Widgets
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))

#Unlink a Widget
mylink.unlink()

#Connecting two Widgets
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'max'))