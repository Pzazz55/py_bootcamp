'''
Built-in Functions & Operator keywords in Python.

Generator is a special type of function that would generate information instead of saving it
into the memory.
- Range
- Enumerate
- Zip (opposite of Enumerate function)
- in
- min
- max
- random
- input
'''

#Test 1a - Range Function
mylist = [1, 2, 3]
print("### Program to demonstrate Range Function - 1a ###")
for num in range(3, 10):
    print(num)

#Test 1b - Range Function, with Step Size
print("### Program to demonstrate Range Function, with Step Size - 1b ###")
for num in range(0, 10, 2):
    print(num)

#Test 1c - Range Function, with Step Size
print("### Program to demonstrate Range Function as a list - 1c ###")
print(list(range(0, 11, 2)))

#Test 2a - Enumerate Function
print("### Program to demonstrate index/letter of a word - 2a ###")
index_count = 0
for letter in 'abcde':
    #print(f'At index {index_count} the letter is {letter}')
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

#Test 2b - Enumerate Function
print("### Program to demonstrate index/letter of a word - 2b ###")
index_count = 0
word = 'abcde'
for letter in word:
    #print(word[index_count])
    #print('At index {} the letter is {}'.format(index_count, letter))
    print('At index {} the letter is {}'.format(index_count, word[index_count]))
    index_count += 1

#Test 2c - Enumerate Function
print("### Program to demonstrate index/letter of a word using Enumerate Function (as tuples) - 2c ###")
#Enumerate function does the index count automatically in the form of tuples.
word = 'abcde'
for letter in enumerate(word):
    print(letter)

#Test 2d - Enumerate Function
print("### Program to demonstrate index/letter of a word using Enumerate Function (as tuples) - 2d ###")
#Enumerate function does the index count automatically in the form of tuples.
#Enumerate function can take in  any sort of iterable object (not just string) and
# will return index counter and the object itself.
word = 'abcde'
for index, letter in enumerate(word):
    print(f'{index} is the index for the letter {letter}')

#Test 3a - Zip Function
print("### Program to demonstrate Zip Function, two lists - 3a ###")
#Zip function zips/pair-up together two lists.
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
for item in zip(mylist1, mylist2):
    print(item)

#Test 3b - Zip Function
print("### Program to demonstrate Zip Function, more than two lists - 3b ###")
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
mylist3 = [100, 200, 300, 400.1, 500.5]
for item in zip(mylist1, mylist2, mylist3):
    print(item)

#Test 3c - Zip Function
print("### Program to demonstrate Zip Function, with uneven lists - 3c ###")
#Zip function will only go and zip together as far as the list which is the shortest, and will
# ignore everything that is extra.
mylist1 = [1, 2, 3, 4, 5, 6, 7, 9, 10]
mylist2 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist3 = [100, 200, 300, 400.1, 500.5]
for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2)))

#Test 3d - Zip Function & Tuple Unpacking
print("### Program to demonstrate Zip Function & Tuple unpacking - 3d ###")
mylist1 = [1, 2, 3, 4, 5, 6, 7, 9, 10]
mylist2 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist3 = [100, 200, 300, 400.1, 500.5]
for a, b, c in zip(mylist1, mylist2, mylist3):
    print(b)

#Test 4a - In Keyword
print("### Program to demonstrate 'in' keyword - 4a ###")
#'in' keyword usage in list
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
#'in' keyword usage in string
print('a' in 'The World is a small place')
#'in' keyword usage in dictionary
print('mykey' in {'mykey': 345})

#Test 4b - In Keyword
print("### Program to demonstrate 'in' keyword in dictionary - 4b ###")
d = {'mykey1': 345, 'mykey2': 456}
if 456 in d.values():
    print("In Values")
if 'mykey1' in d.keys():
    print("In Keys")

#Test 5a - 'min' & 'max' function
print("### Program to demonstrate 'min' & 'max' keyword - 5a ###")
mylist = [40, 20, 35, 15, 100]
print(f'The minimum of the list is {min(mylist)}')
print(f'The minimum of the list is {max(mylist)}')

#Test 6a - 'Random' Library
print("### Program to demonstrate 'random' liberary - 6a ###")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Python comes with built-in Random Library.
#First, we need to import from the Random library and then call the shuffle function.
from random import shuffle
#print(shuffle(mylist)) #this does not return any value and the type is defined as 'None'
shuffle(mylist) #this is an inplace function - that operates inplace
print(mylist)

#Test 6b - 'Random' Library
print("### Program to grab a random integer between a range - 6b ###")
from random import randint
ran = randint(0, 100)
print(f'The random number is {ran}')

#Test 7a - Taking user input.
#input always accepts as a string.
print("### Program to take user input - 7a ###")
uname = input("Enter your Name: ")
print(type(uname))
print(f"The name of the person is {uname}.")

#Test 7b - Taking user input and casting it.
print("### Program to take user input and casting it - 7a ###")
a = int(input("Enter a Number: "))
print(type(a))
print(f"The number entered is {a}.")