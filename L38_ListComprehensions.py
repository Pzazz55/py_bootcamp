'''
List Comprehensions in Python
- List Comprehensions are a unique way of quickly creating a list in Python.
If you find yourself using a for loop along with .append() to create a list, then list comprehensions
are a good alternative.

'''
#Test 1 - Appending to a list, using for loop.
print("### Program to appending to a list, using for loop - 1 ###")
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

#Test 2 - Appending to a list, using list Comprehensions.
print("### Program to appending to a list, using list comprehensions - 2 ###")
mystring = 'hello'
#for letter in mystring:
#    mylist.append(letter)
#the above two lines are replaced with the below single line - flattened out the for loop.
mylist = [letter for letter in mystring]
print(mylist)

#Test 3 - List Comprehensions
print("### Program to demonstrate list comprehensions - 3 ###")
print([x for x in 'wordtwo'])
print([x for x in range(0, 11)])

#Test 4 - List Comprehensions, with operations on the variable.
print("### Program to demonstrate list comprehensions, with operations on the variable - 4 ###")
print("The square of numbers in a range is: ")
print([x**2 for x in range(0, 11)])

#Test 5 - List Comprehensions, with 'if' statement.
print("### Program to demonstrate list comprehensions, with 'if' statement - 5 ###")
print("The list of even numbers in the range is: ")
print([x for x in range(0, 11) if x % 2 == 0])
print("The square of even numbers in the range is: ")
print([x**2 for x in range(0, 11) if x % 2 == 0])

#Test 6 - List Comprehensions - more examples.
print("### Program to convert celsius into fahrenheit - 6 ###")
celsius = [1, 10, 20, 34.5]
print("The temperature in fahrenheit is: ")
print([((9/5)* temp + 32) for temp in celsius])

#Test 7 - List Comprehensions, with 'if-else' statement.
print("### Program to demonstrate list comprehensions, with 'if-else' statement - 7 ###")
print("The list of even numbers in the range is: ")
print([x if x%2 == 0 else 'ODD' for x in range(0,11)])

#Test 8a - Nested loop (without List Comprehensions)
print("### Program to demonstrate Nested Loop, without List Comprehensions - 8a ###")
mylist = []
for x in [2, 4, 6]:
    for y in [10, 200, 300]:
        mylist.append(x*y)
print(mylist)

#Test 8b - List Comprehensions, with Nested loop.
print("### Program to demonstrate list comprehension, with Nested loop - 8b ###")
print([x*y for x in [2, 4, 6] for y in [10, 200, 300]])