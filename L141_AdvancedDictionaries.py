'''
**********************************************************************************************************
Working with Advanced Python Objects - Lesson 138 to 144
**********************************************************************************************************
The below script demonstrates 'Advanced Dictionaries':
- Dictionary Comprehensions
- iteritems, itervalues, iterkeys, viewitems, viewkeys, viewvalues (Python 2)
**********************************************************************************************************
'''

#just like list comprehensions, dictionaries also support their version of comprehensions (though not very common in use)
#creating a dictionary through the dictionary comprehension.
print("The below is a dictionary created using 'Dictionary Comprehension'::")
d1 = {x: x**2 for x in range(10)} 
print(d1)

#inorder to assign keys that are not based on values, use zip
print("The below is a dictionary created using 'Dictionary Comprehension'::") 
d2 = {k: v**2 for k, v in zip(['a', 'b'], range(2))}
print(d2)

d3 = {'k1': 1, 'k2': 2}
#the below 'iter' method only works in Python 2 version.
print("The below is to fetch items from the dictionary using 'iter' keywords ::")
for k in d3.iteritems():
    print(k)
    
for k in d3.itervalues():
    print(k)

for k in d3.iterkeys():
    print(k)

#the below 'view' methods only works in Python 2 version.
print("The below is to view items from the dictionary using 'view' keywords ::")
d3.viewitems()
d3.viewkeys()
d3.viewvalues()