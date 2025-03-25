'''
For Loops
'''

# Test 1
print("### Program to show 'for' loop ###")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for jelly in mylist:
    print(jelly)

# Test 2
print("### Program to show 'for' loop ###")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for jelly in mylist:
    print("Hello")

# Test 3 - Checking the Even Number
print("### Program to print the Even/Odd number using 'for' loop ###")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    #Check for Even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

#Test 4 - Keeping a running tally of multiple loops
#This can also be achieved using enumerate function.
print("### Program to show the running tally of the numbers in the list. ###")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0
for num in mylist:
    list_sum += num
    print(f'The running tally of the numbers in the list is : {list_sum}, for iteration # {num}')

print(f'The sum of the numbers in the list is : {list_sum}')

#Test 5 - Iterating over a String
# Strings are sequence, and we can iterate through them. We can be accessing each character in the string.
# Approach # 1
print("### Program to show iteration over a String. ###")
print("Printing letters in a String using 'for' loop.")
mystring = 'Hello World'
for letter in mystring:
    print(letter)

# Approach # 2
print("### Program to print the letters in a String, using 'for' loop. ###")
print("Printing letters in a String using 'for' loop.")
for letter in 'Hello World':
    print(letter)

#Test 6 - Variable in 'for' loop
print("### Program to show '_' as a iterator in the 'for' loop. ###")
for _ in 'Hello World':
    print('Cool !')

#Test 7 - Iterating over a tuple.
tup = (1, 2, 3)
print ("### Program for iterating over a tuple. ###")
for items in tup:
    print(tup)
    print(items)

#Test 8 - Tuple Unpacking - Approach 1
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print ("### Program for Tuple Unpacking. ###")
print (f'The length of the list is - {len(mylist)}')
for item in mylist:
    print(item)

#Test 8 - Tuple Unpacking - Approach 2
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print ("### Program for Tuple Unpacking. ###")
print (f'The length of the list is - {len(mylist)}')
#for a,b in mylist:
for (a,b) in mylist:
    print(a)
    #print(b)

#Test 9 - Tuple Unpacking - Approach 1
mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
print ("### Program for Tuple Unpacking. ###")
for item in mylist:
    print(item)

#Test 9 - Tuple Unpacking - Approach 2
mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
print ("### Program for Tuple Unpacking. ###")
print (f'The length of the list is - {len(mylist)}')
#for a,b,c in mylist:
for (a,b,c) in mylist:
    print(b)

#Test 10 - Iterating through a Dictionary - #1
d = {'k1':1, 'k2':2, 'k3':3}
print ("### Program for iterating over a Dictionary - 1. ###")
#Print the Dictionary Values.
for item in d:
    print(item)

#Test 10 - Iterating through a Dictionary - #2
d = {'k1':1, 'k2':2, 'k3':3}
print ("### Program for iterating over a Dictionary - 2. ###")
#Print the Dictionary Pairs.
for item in d.items():
    print(item)

#Test 10 - Iterating through a Dictionary - #3a
d = {'k1':1, 'k2':2, 'k3':3}
print ("### Program for iterating over a Dictionary - 3a. ###")
#Print the Dictionary Values or Keys.
for key, value in d.items():
    print(value)

#Test 10 - Iterating through a Dictionary - #3b
d = {'k1':1, 'k2':2, 'k3':3}
print ("### Program for iterating over a Dictionary - 3b. ###")
#Print the Dictionary Values or Keys.
for val in d.values():
    print(val)

#Note: Dictionaries are Unordered.