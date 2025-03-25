'''
Generator functions allow us to write a function that can send back a value and then later resume to pick up
where it left off.
This type of function is a generator in Python, allowing us to generate a sequence of values over time.
When a generator function is complied they become an object that supports an iteration protocol.
That means when they are called in your code they don't actually return a value and then exit. Instead, the generator
functions will automatically suspend and resume their execution and state around the last point of value generation.
The advantage is that instead of having to compute an entire series of values up front, the generator computes one value
waits until the next value is called for.
Example of a generator function is a range function.
'''
#Program 1a: Program to demonstrate Generators.
def create_cubes(n):
    results = []
    for x in range(n):
        results.append(x**3)
    return results

print("***** Program to demonstrate Generators - Example 1a ******")
print(create_cubes(10)) #all the values are fetched and stored in the memory.

for x in create_cubes(10):
    print(x) #Note here, we are only fetching one value at a time and don't need the whole list to be stored in the memory.

#Program 1b: Program to demonstrate Generators.
def create_cubes(n):
    for x in range(n):
        yield x**3

print("***** Program to demonstrate Generators - Example 1b ******")
print(create_cubes(10)) #returns the location of the memory where the list object is created.
# We need to iterate through it if we need the actual list of numbers.
print(list(create_cubes(10)))
for x in create_cubes(10):
    print(x)

#Program 2: Program to demonstrate Fibonaci Sequence using Generators.
def gen_fibon(n):
    a, b = 1, 1
    for x in range(n):
        yield a
        # a, b, = b, a+b
        a = b
        b = a+b

print("***** Program to demonstrate Fibonaci Sequence using Generators. - Example 2 ******")
print(list(gen_fibon(10)))

#Program 3: Program to demonstrate Next function using Generators.
def simple_gen():
    for x in range(3):
        yield x

print("***** Program to demonstrate Next function using Generators. - Example 3 ******")
print(list(simple_gen()))
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
#the above is what the generator object is doing when we call the yield keyword.

#Program 4: Program to demonstrate iter objects using Generators.
s = 'hello'

print("***** Program to demonstrate the iter objects using Generators - Example 4 ******")
for letter in s:
    print(letter)

#next(s)
print("Note, we cannot use next to iterate on a string. It should be a generator inorder to iterate using next.")
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))




