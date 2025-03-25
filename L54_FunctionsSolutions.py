
'''
Programming Practise using Functions - Challenging Problems
'''

#**********************************************************************************************************#
#SPY GAME: Write a function that takes in a list of integers and returns 'True' if it contains 007 in order.
#**********************************************************************************************************#

#Program - 1a Approach - 1
def syp_game(myList):
    str = []
    for i in range(0, len(myList)):
        if myList[i] == 0 or myList[i] == 7:
            str.append(myList[i])
        else:
            continue
    if str == [0, 0, 7]:
        return True
    else:
        return False

print("SYP GAME - Approach 1")
print(syp_game([1, 2, 4, 0, 0, 7, 5]))
print(syp_game([1, 0, 2, 4, 0, 5, 7]))
print(syp_game([1, 7, 2, 0, 4, 5, 0]))

#Program - 1b Approach - 2
def syp_games(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print("SYP GAME - Approach 2")
print(syp_games([1, 2, 4, 0, 0, 7, 5]))
print(syp_games([1, 0, 2, 4, 0, 5, 7]))
print(syp_games([1, 7, 2, 0, 4, 5, 0]))

#**********************************************************************************************************#
#COUNT PRIME: Write a function that returns the number of prime numbers that exists up to and including a given number
#**********************************************************************************************************#

#Program - 1a Approach - 1
def count_prime(num1, num2):
    primeList = [0, 1]
    z = True
    for x in range(num1, num2):
        #print(num1, num2)
        for y in range (2, x):
            #print(x, y)
            if x % y == 0:
                z = True
                break
            else:
                z = False

        if z == False:
            primeList.append(x)
    print(primeList)
    return len(primeList)

print("COUNT PRIME - Approach 1")
print(count_prime(2, 100))

# For more complex math and programming problems, visit the below website.
# https://projecteuler.net/