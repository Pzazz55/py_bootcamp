'''
Methods and Functions Homework Problems
'''
import string

#Program 1 - Write a function to calculate the volume of a sphere given its radius.
def fun_volume(rad):
    return ((rad ** 3)*(3.14)*(4/3))

print("****** Write a function to calculate the volume of a sphere given its radius ******")
print(fun_volume(2))


#Program 2a - Write a function that checks whether a number is in a
# given range (inclusive of highs and lows).
def fun_findnum(num, low, high):
    if num >= low and num <= high:
        return f"{num} is in the given range - {low} and {high}."
    else:
        return f"{num} is not in the given range - {low} and {high}."

print("****** Write a function that checks whether a number is in a given range ******")
print(fun_findnum(2, 1, 5))
print(fun_findnum(7, 1, 5))

#Program 2b - Write a function that checks whether a number is in a
# given range (inclusive of highs and lows).
def fun_findnum(num, low, high):
    if num in range(low, high+1):
        return f"{num} is in the given range - {low} and {high}."
    else:
        return f"{num} is not in the given range - {low} and {high}."

print("****** Write a function that checks whether a number is in a given range ******")
print(fun_findnum(2, 1, 5))
print(fun_findnum(7, 1, 5))


#Program 3a - Write a function that accepts a string and calculates the number of upper cases
# letters and lower cases letters.
def fun_upperlower(mystr):
    i, upp, low = 0, 0, 0
    for i in range(len(mystr)):
        if mystr[i].isupper():
            upp += 1
        elif mystr[i].islower():
            low += 1
        else:
            pass

    print(f"In the given string - {mystr}.")
    print(f"The number of upper case characters is {upp}.")
    print(f"The number of lower case characters is {low}.")

print("****** Write a function that calculates the number of upper and lower case letters - 3a ******")
fun_upperlower('Nahush VivasVat')
fun_upperlower('Hello Mr. Kumar, How are you this Wednesday?')

# Program 3b - Write a function that accepts a string and calculates the number of upper cases
# letters and lower cases letters.
def fun_upperlower(mystr):
    char, upp, low = '', 0, 0
    for char in mystr:
        if char.isupper():
            upp += 1
        elif char.islower():
            low += 1
        else:
            pass

    print(f"In the given string - {mystr}.")
    print(f"The number of upper case characters is {upp}.")
    print(f"The number of lower case characters is {low}.")

print("****** Write a function that calculates the number of upper and lower case letters - 3b ******")
fun_upperlower('Nahush VivasVat')
fun_upperlower('Hello Mr. Kumar, How are you this Wednesday?')

# Program 3b - Write a function that accepts a string and calculates the number of upper cases
# letters and lower cases letters.
def fun_upperlower(mystr):
    d = {'upp': 0, 'low': 0}
    char = ''
    for char in mystr:
        if char.isupper():
            d['upp'] += 1
        elif char.islower():
            d['low'] += 1
        else:
            pass

    print(f"In the given string - {mystr}.")
    print(f"The number of upper case characters is {d['upp']}.")
    print(f"The number of lower case characters is {d['low']}.")

print("****** Write a function that calculates the number of upper and lower case letters - 3c ******")
fun_upperlower('Nahush VivasVat')
fun_upperlower('Hello Mr. Kumar, How are you this Wednesday?')

#Program 4a - Write a function that takes a list and returns a new list with unique elements of
# the first list.
def fun_uniquelist(mylist):
    newset = set(mylist)
    newlist = list(newset)
    return newlist
    # return list(set(mylist))

print("****** Write a function that returns a new list with unique elements - 4a ******")
newlist = fun_uniquelist([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 1, 3, 4, 4, 5, 4, 5, 4])
print(newlist)

#Program 4b - Write a function that takes a list and returns a new list with unique elements of
# the first list.
def fun_uniquelist(mylist):
    newlist = []
    for num in mylist:
        if num not in newlist:
            newlist.append(num)
    return newlist

print("****** Write a function that returns a new list with unique elements - 4b ******")
newlist = fun_uniquelist([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 1, 3, 4, 4, 5, 4, 5, 4])
print(newlist)

#Program 5 - Write a function to multiply all the numbers in the list.
def fun_multiplylist(mylist):
    mul, i = 1, 0
    for i in range(0, len(mylist)):
        mul = mul * mylist[i]
    return mul

print("****** Write a function to multiply all the numbers in the list ******")
num = fun_multiplylist([1, 2, 3, -4])
print(f"The multiplication of the numbers in the list is {num}")

#Program 6 - Write a function to check whether a word or phrase is palindrome or not.
def fun_ispalindrome(str):
    str = str.replace(' ','')
    newstr = str[::-1]
    if str == newstr:
        return "The word or phrase that is sent is a palindrome"
    else:
        return "The word or phrase that is sent is not a palindrome"

print("****** Write a function to check whether a word or phrase is palindrome or not ******")
print(fun_ispalindrome('Hell olleH'))
print(fun_ispalindrome('nurses run'))

#Program 7a - Write a function to check whether a string is Pangram or not.
#Pangram - Pangrams are words or sentences containing every letter of the alphabets at least once.
def fun_ispangram(inp_str):
    inp_str = inp_str.lower()
    inp_str_set = set(inp_str.replace(" ",""))

    # alpha_str = 'abcdefghijklmnopqrstuvwxyz'
    alpha_str = string.ascii_lowercase #alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_str_set = set(alpha_str)

    result = alpha_str_set.issubset(inp_str_set)  # Checks if all the items in the set X are present in Y => if Yes, returns True.
    if result is True:
        return "This is a Pangram Word or Sentence"
    else:
        return "This is a not a Pangram Word or Sentence"

print("****** Write a function to check whether a word or phrase is palindrome or not - 7a ******")
print(fun_ispangram("The quick brown fox jumps over the lazy dog."))

#Program 7b - Write a function to check whether a string is Pangram or not.
#Pangram - Pangrams are words or sentences containing every letter of the alphabets at least once.
def fun_ispangram(inp_str):
    inp_str = inp_str.lower()
    inp_str_set = set(inp_str.replace(" ",""))

    # alpha_str = 'abcdefghijklmnopqrstuvwxyz'
    alpha_str = string.ascii_lowercase #alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_str_set = set(alpha_str)

    if alpha_str_set == inp_str_set:
        return "This is a Pangram Word or Sentence"
    else:
        return "This is a not a Pangram Word or Sentence"

print("****** Write a function to check whether a word or phrase is palindrome or not - 7b ******")
print(fun_ispangram("The quick brown fox jumps over the lazy dog."))