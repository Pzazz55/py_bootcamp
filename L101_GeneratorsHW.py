import random


#Program 1: Program to create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for x in range(N):
        yield x**2

print("***** Program to create a generator that generates the squares of numbers up to some number N ******")
for x in gensquares(10):
    print(x)

#Program 2: Program to create a generator that yields "n" random numbers between a low and high number (that are inputs).
def rand_num(low, high, num):
    for i in range(num):
        yield random.randint(low, high)

print("***** Program to create a generator that yields random numbers between a low and high number ******")
for x in rand_num(10, 100, 5):
    print(x)

#Program 3: Program to use the iter() function to convert the string into an iterator.
s = 'hello'
sgen = iter(s)

print("***** Program to use the iter() function to convert the string into an iterator. ******")
print(next(sgen))
print(next(sgen))
print(next(sgen))

#Program 4: Program to demonstrate Generator Comprehension.
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)

print("***** Program to demonstrate Generator Comprehension. ******")
for item in gencomp:
    print(item)
