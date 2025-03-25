'''
Python has a inbuilt debugger tool that allows you to interactively explore variables within
mid-operation of the python code.
'''
import pdb #Python Debugger

x = [1, 2, 3]
y = 2
z = 3

result_one = y + z
pdb.set_trace()
result_two = x + y