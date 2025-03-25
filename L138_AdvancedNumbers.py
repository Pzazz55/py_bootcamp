'''
**********************************************************************************************************
Working with Advanced Python Objects - Lesson 138 to 144
**********************************************************************************************************
The below script demonstrates 'Advanced Numbers':
- hexadecimal number formating - hex built in function to convert a number to hexadecimal
- binary number formating - bin built in function to convert a number to binary
- built in arguments - pow(), abd, round
**********************************************************************************************************
'''

print("\n##### Hexadecimal Numbers #####")
print("Hexadecimal value for 12 is ::", hex(12))
print("Hexadecimal value for 512 is ::", hex(512))

print("\n##### Binary Numbers #####")
print("Binary value for 1234 is ::", bin(1234))
print("Binary value for 128 is ::", bin(128))
print("Binary value for 512 is ::", bin(512))

print("\n##### Power of Value #####")
print("The value of 2**4 is ::", 2**4)
print("The value of 2**4 is ::", pow(2, 4)) #with two arguments, it equals x**y
print("The value of (2**4) % 3 is ::", pow(2, 4, 3)) #with two arguments, it equals (x**y) % z

print("\n##### Absolute of Value #####")
print("The absolute value of 2 is ::", abs(2))

print("\n##### Rounding of Value #####")
print("The rounded value of 3.13 is ::", round(3.13))
print("The rounded value of 3.93 is ::", round(3.93))
print("Rounding to the decimal places ::", round(3.141592, 2))