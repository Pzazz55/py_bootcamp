'''
**********************************************************************************************************
Working with Advanced Python Objects - Lesson 138 to 144
**********************************************************************************************************
The below script demonstrates 'Advanced Lists':
- append, count, extend, index, insert, pop, remove, reverse, sort
**********************************************************************************************************
'''

#APPEND
print('###### APPEND ######')
l = [1, 2, 3]
print("The list before append is ::", l)
l.append(4)
print("The list after append is ::", l)

#COUNT
print('\n###### COUNT ######')
print("To show the count of elements in the list ::")
print(l.count(10))
print(l.count(1))

#APPEND
print('\n###### APPEND ######')
x = [1, 2, 3]
x.append([4, 5])
print("To add a list as an element inside another list::")
print(x)

#EXTEND
print('\n###### EXTEND ######')
x = [1, 2, 3]
x.extend([4, 5])
print("To extend the original list with each element from another list::")
print(x)

#INDEX
print('\n###### INDEX ######')
print("To print the index of an element ::")
print(l.index(2))

#INSERT
print('\n###### INSERT ######')
l = [1, 2, 3, 4]
print("The list before insert is ::", l)
#insert - takes in two arguments (index and object). It places the object at the index applied
l.insert(2, 'inserted')
print("The list after insert is ::", l)

#POP
print('\n###### POP ######')
#pop is inplace (the changes will be permanent)
print("The list before pop is ::", l)
ele = l.pop()
print("The element that is popped out is", ele)
print("The list after pop is ::", l)

#we can pass an index into the pop
print("The list before pop is ::", l)
ele = l.pop(2)
print("The element that is popped out is", ele)
print("The list after pop is ::", l)

#REMOVE
print('\n###### REMOVE ######')
ls = [1, 4, 5, 2, 4, 'text1', 4, 2, 6, 9, 'text1']
#remove - to remove the first occurance of the value
print("The list before remove is ::", ls)
ls.remove(4)
print("The list after remove is ::", ls)

#REVERSE
print('\n###### REVERSE ######')
#reverse is inplace (the changes will be permanent)
print("The list before reverse is ::", ls)
ls.reverse()
print("The list after reverse is ::", ls)

#SORT
print('\n###### SORT ######')
ls = [8, 4, 2, 5, 1, 7, 3]
#sort is inplace (the changes will be permanent)
print("The list before sort is ::", ls)
ls.sort()
print("The list after sort is ::", ls)
