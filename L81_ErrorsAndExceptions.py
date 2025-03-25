'''
Example Problems
'''

#Example - 1
print("### Program to demonstrate TRY//EXCEPT - Example 1 ###")
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print('Enter an Integer')

#Example - 2
print("### Program to demonstrate TRY//EXCEPT//FINALLY - Example 2 ###")
x = 5
y = 0
try:
    z = x / y
except:
    print('There is an error in the code')
finally:
    print("All done")

#Example - 3

def ask():
    while True:
        try:
            x = int(input("Enter an Integer: "))
        except:
            print('This is not an Integer. Try Again !')
            continue
        else:
            print(f"The square of the number is: {x ** 2}")
            break
        finally:
            print("All done")

print("### Program to demonstrate TRY//EXCEPT//FINALLY - Example 3 ###")
ask()