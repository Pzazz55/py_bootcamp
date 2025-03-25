'''
Programming Practise using Functions - Level 2
'''

#**********************************************************************************************************#
#FIND 33: Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
#**********************************************************************************************************#

#Program - 1a Approach - 1
def myfunc(myList):
    for val in range(0, len(myList) - 1):
        if myList[val] == 3 and myList[val+1] == 3:
            return True
            break
    return False

print("Given a list of integers, return True if the array contains a 3 next to a 3 somewhere - 1a")
x = myfunc([1, 3, 3]) #returns True
print(x)
x = myfunc([1, 3, 1, 3]) #returns False
print(x)
x = myfunc([3, 1, 3, 3, 3, 1]) #returns False
print(x)

#Program - 1b Approach - 2
def myfunc(myList):
    for val in range(0, len(myList) - 1):
        if myList[val:val+2] == [3,3]:  #Another way of writing myList[val] == 3 and myList[val+1] == 3:
            return True
            break
    return False

print("Given a list of integers, return True if the array contains a 3 next to a 3 somewhere - 1b")
x = myfunc([1, 3, 3]) #returns True
print(x)
x = myfunc([1, 3, 1, 3]) #returns False
print(x)
x = myfunc([3, 1, 3, 3, 3, 1]) #returns False
print(x)

#**********************************************************************************************************#
#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters.
#**********************************************************************************************************#

#Program - 2 Approach - a & b
def paper_dollFirstApproach(myList):
    NewList = []
    for letter in myList:
        NewList.append(letter)
        NewList.append(letter)
        NewList.append(letter)
    return ' '.join(NewList)  #converting a list to string

def paper_dollSecondApproach(myList):
    newStr = ""
    for letter in myList:
        newStr += letter * 3 # can also be written as newStr += letter + letter + letter
    return ' '.join(newStr)  #converting a list to string

print("Given a string, return a string where for every character in the original there are three characters - 2a")
print(paper_dollFirstApproach('Hello'))
print(paper_dollFirstApproach('Mississippi'))
print("Given a string, return a string where for every character in the original there are three characters - 2b")
print(paper_dollSecondApproach('Hello'))
print(paper_dollSecondApproach('Mississippi'))

#**********************************************************************************************************#
#BLACk JACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#**********************************************************************************************************#

#Program - 3a Approach - 1
def check_input(num):
    if num >= 1 and num <= 11:
        return True
    else:
        return False

def check_sum(num1, num2, num3):
    if check_input(num1) == True and check_input(num2) == True and check_input(num3) == True:
        tot = num1 + num2 + num3
        if tot <= 21:
            return tot
        else:
            if num1 == 11 or num2 == 11 or num3 == 11:
                tot = tot - 10
                if tot <= 21:
                    return tot
                else:
                    return "BUST"
            else:
                return "BUST"
    else:
        print("Invalid Inputs")
        return 0

print("Black Jack Program - 3 Approach 1")
print(check_sum(5, 6, 7))
print(check_sum(9, 9, 9))
print(check_sum(9, 9, 11))

#Program - 3b Approach - 2

def blackjack(num1, num2, num3):
    if sum([num1, num2, num3]) <= 21:
        return sum([num1, num2, num3])
    elif 11 in [num1, num2, num3] and sum([num1, num2, num3]) - 10 <= 21:
        return sum([num1, num2, num3]) - 10
    else:
        return "BUST"
print("Black Jack Program - 3 Approach 2")
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

#**********************************************************************************************************#
#SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with
#a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no number.
#**********************************************************************************************************#

#Program - 4a Approach - 1

def summer_69(myList):
    sum = 0
    flag = True
    for i in range(0, len(myList)):
        while flag == True:
            if myList[i] != 6:
                sum += myList[i]
                break
            else:
                flag = False

        while flag == False:
            if myList[i] != 9:
                break
            else:
                flag = True
                break
    return sum
print("SUMMER OF 69 - Approach 1")
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
