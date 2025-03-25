'''
Computers use something called as Pseudo Random Number generators to come up with Random Numbers. However, this is beyond the scope of study here.
'''

import random

print(random.randint(1, 100)) #check a random integer in range a & b, and it includes both endpoints.

random.seed(101)
#if two programmers set the same seed number then the program will return the same random number.
#running the above program again-and-again will return the same random number.
print(random.randint(0, 100)) #74
print(random.randint(0, 100)) #24
print(random.randint(0, 100)) #69
print(random.randint(0, 100)) #45
print(random.randint(0, 100)) #59

myList = list(range(0, 20))
print(f"The list is: {myList}")
print(f"A random value chosen from the list is: {random.choice(myList)}")

#sampling a list with replacement/with repetition.
print(f"The random sample from the list is: {random.choices(population=myList,k=10)}")
#it randomly picks numbers from the list (does 10 times) and put that into a list. Here, we can see that the numbers are being repeated.

#sampling a list without replacement/without repetition.
print(f"The random sample from the list without replacement is: {random.sample(population=myList,k=10)}")

newList = list(range(0, 25))
print(f"The list is: {newList}")
random.shuffle(newList)
print(f"The list after inplace suffling is: {newList}") #inplace suffling and impacts the original list.

print(f"Uniform distribution random value is: {random.uniform(0, 100)}") #it shows a floating point value.
print(f"Guassian or Normal Distribution of random value is: {random.gauss(mu=0, sigma=1)}") #it takes mean and Standard Deviation as parameters.
