'''
Programming Practise using Functions
'''

#**********************************************************************************************************
#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd.
#**********************************************************************************************************

#Test 1a - Approach 1
def myfuncLess(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

def myfuncHigh(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.")
print("### This is program number 1 - approach 1 ###")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    ans = myfuncLess(num1, num2)
else:
    ans = myfuncHigh(num1, num2)

print(ans)


#Test 1b - Approach 2

def myfunc(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)

print("### This is program number 1 - approach 2 ###")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))

print(myfunc(num1, num2))



#***********************************************************************************************************
#ANIMAL CRACKERS: Write a function that takes two-word string and returns True if both words begin with same letter.
#**********************************************************************************************************


#Test 2a - Approach 1
def animal_cracker(str1, str2):
    if str1[0] == str2[0]:
        return True
    else:
        return False

print("Write a function that takes two-word string and returns True if both words begin with same letter.")
print("### This is program number 2 - approach 1 ###")
name1 = input("Enter a Name: ")
name2 = input("Enter another Name: ")

print(animal_cracker(name1, name2))

#Test 2a - Approach 2
def animal_cracker(names):
    wordlist = names.lower().split()
    return wordlist[0][0] == wordlist [1][0]

print("### This is program number 2 - approach 2 ###")
names = input("Enter two Names: ")
print(animal_cracker(names))

#***********************************************************************************************************
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integer is 20.
#If not, return False.
#**********************************************************************************************************

#Test 3a - Approach 1
def myfunc(num1, num2):
    if num1 == 20 or num2 == 20 or (num1+num2) == 20:
        return True
    else:
        return False

print("Given two integers, return True if the sum of the integers is 20 or if one of the integer is 20. If not, return False.")
print("### This is program number 3 - approach 1 ###")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))

print(myfunc(num1, num2))

#Test 3b - Approach 2
def myfunc(num1, num2):
    return num1 == 20 or num2 == 20 or (num1+num2) == 20

print("### This is program number 3 - approach 2 ###")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))

print(myfunc(num1, num2))