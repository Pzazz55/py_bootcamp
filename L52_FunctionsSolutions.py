'''
Programming Practise using Functions - Level 1
'''

#**********************************************************************************************************#
#OLD MACDONALD: Write a function that capitalizes the first and fourth letter of a Name.
#**********************************************************************************************************#

#Program - 1
def myfuncFirstApproach(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

def myfuncSecondApproach(name):
    FirstWord = name[:3]
    SecondWord = name[3:]
    return FirstWord.capitalize() + SecondWord.capitalize()

print("Write a function that capitalizes the first and fourth letter of a Name.")
print("### This is program number 1 - approach 1 ###")
name = input("Enter a Name: ")

print(myfuncFirstApproach(name))
print(myfuncSecondApproach(name))

#**********************************************************************************************************#
#MASTER YODA: Give a sentence, return a sentence with the word reversed.
#**********************************************************************************************************#

#Program - 2
def reverse_sentence(str):
    mylist = str.split()
    reverse_mylist = mylist[::-1]
    return reverse_mylist

print("Give a sentence, return a sentence with the word reversed.")
print("### This is program number 2 - approach 1 ###")
str = input("Enter a sentence: ")
x = reverse_sentence(str)
newstr = ' '.join(x)
print(newstr)

# ****************** JOIN Function ****************** #
# mylist = ['a', 'b', 'c']
# print('--'.join(mylist))
# print(' '.join(mylist))
# print('ooo'.join(mylist))

#**********************************************************************************************************#
#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200.
#**********************************************************************************************************#

#Program - 3 Approach - 1
def myfunc(userinput, level):
    # print(userinput, level)
    if userinput < level - 10:
        return False
    elif userinput > level + 10:
        return False
    else:
        return True

print("Given an integer n, return True if n is within 10 of either 100 or 200.")
num = int(input("Enter a Number: "))
x = myfunc(num, 100)
y = myfunc(num, 200)
print(x or y)


# Program - 3 Approach - 2
def myfunc(userinput):
    return (abs(100 - userinput) <= 10) or (abs(200 - userinput) <= 10)
    #abs (Absolute Value Function) returns the absolute value of a number.

print("Given an integer n, return True if n is within 10 of either 100 or 200.")
num = int(input("Enter a Number: "))
print(myfunc(num))