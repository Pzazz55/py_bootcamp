
'''
Functions with Logic
'''

# Test 1a - Write a function to check if a give number is even or odd.
def even_odd_check(num):
    if num % 2 == 0:
        print(f'{num} is an Even Number.')
    else:
        print(f'{num} is an Odd Number.')

print("### Program to check if a given number is even or odd - 1a ###")
x = int(input("Enter a number to check if it Even or Odd: "))
even_odd_check(x)


# Test 1b - Write a function to return true if a give number is Even or Odd.
def even_check(num):
    return num % 2 == 0

print("### Program to check if a given number is even or odd - 1b ###")
print(even_check(44))

# Test 2 - Write a function to return true if any number is Even inside a list.
def check_even_list(numlist):
    for number in numlist:
        if number % 2 == 0:
            return True
        else:
            pass
    return False

print("### Program to check if a given list has even numbers inside it - 2 ###")
print(check_even_list([1, 3, 7, 15, 17, 19]))   #Odd - False
print(check_even_list([1, 3, 7, 15, 17, 18]))   #Even - True
print(check_even_list([18, 3, 7, 15, 17, 18]))  #Even - True
print(check_even_list([18, 3, 7, 15, 17, 1]))   #Even - True
print(check_even_list([1]))                     #Odd - False
print(check_even_list([4]))                     #Even - True

# Test 3 - Write a function to return all the even numbers in the list.
def check_even_num(numlist):
    even_num = [] #placeholder variable
    for number in numlist:
        if number % 2 == 0:
            even_num.append(number)
        else:
            pass
    return even_num

print("### Program to return all the even numbers in the list - 3 ###")
retlist = check_even_num([1, 2, 7, 14, 17, 18])
print(retlist)

retlist = check_even_num([18])
print(retlist)

retlist = check_even_num([1, 3, 5])
print(retlist)
