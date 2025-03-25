'''
Lambda Expressions are a quick way to create Anonymous Functions. A one-time use functions
that we don't need to name and just use it one-time only, and are never reference again.
Lamda Expressions should be used when they can be easily read - if we have to come back to
the code later.

Map Function (Built-In Function) - A map function passes the function that every single
element/item in the list.

Filter Function (Built-In Function) - A filter function returns the iterator
yielding those items of the iterable for which we pass in the item to the function which
is True. This means we need to filter by a function which either returns a True or False.
'''

#Program 1
def square(num):
    return num**2

print("***** Program to demonstrate Map Function *****")
my_nums = [1, 2, 3, 4, 5]
#a map function passes the function that every single element/item in the list.
map(square, my_nums) #returns a memory location

#Approach 1
print("Approach # 1")
for item in map(square, my_nums):
    print(item)

#Approach 2
print("Approach # 2")
print(list(map(square, my_nums))) #returns the list

#Program 2
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

print("***** Program to demonstrate Map Function *****")
names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

#Program 3
def check_even(num):
    return num % 2 == 0

print("***** Program to demonstrate Filter Function *****")
mynums = [1, 2, 3, 4, 5, 6]

#map applies the function to every item in the list.
#filter instead will go and filter based of the function condition.

#Approach 1
print("Approach # 1")
for n in filter(check_even, mynums):
    print(n)

#Approach 2
print("Approach # 2")
print(list(filter(check_even, mynums)))

#Program 4
print("***** Program to demonstrate Lambda Function *****")
print("Approach # 1")
def square(num):
    res = num ** 2
    return res

print(square(3))

print("Approach # 2")
square = lambda num: num ** 2
print(square(3))

#Program 5
print("***** Program to demonstrate Lambda Function along with Map/Filter *****")

print("Lambda with Map Function")
mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda num: num ** 2, mynums)))

print("Lambda with Filter Function")
#Program with lambda and filter function to print the even numbers.
mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda num: num % 2 == 0, mynums)))

#Program with lambda and map function to print the first letter of a list.
names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda str: str[0], names)))

#Program with lambda and map function to reverse and print the names.
names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda str: str[::-1], names)))