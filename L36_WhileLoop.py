'''
While Loops - While loops will continue to execute a block of code while some condition remains True.

Syntax
-----------------------------
while <boolen_condition>:
    #do something
else:
    #do something different

break: breaks out of the current closest enclosing loop.
continue: goes to the top of the closest enclosing loop.
pass: does nothing at all.

'''

#Test 1 - While Loop
x = 0
print("### Program for While Loop - 1 ###")
while x < 5:
    print(f'The current value of x is {x}.')
    #x = x + 1
    x += 1

#Test 2 - While Loop with Else
x = 0
print("### Program for While Loop with Else - 2 ###")
while x < 5:
    print(f'The current value of x is {x}.')
    x += 1
else:
    print("x IS NOT LESS THAN 5.")

'''
#Test 3a - pass keyword
x = [1, 2, 3]
print("### Program to show 'pass' keyword - 3a ###")
for item in x:
    #comments - throws a syntax error because
    #for loop should be followed by a block and not comments.
print ("End of the Script")
'''

# Test 3b - pass keyword
x = [1, 2, 3]
print("### Program to show 'pass' keyword - 3b ###")
for item in x:
    #commnets
    pass
print ("End of the Script")

# Test 4 - continue keyword
mystring = 'Sammy'
print("### Program to show 'continue' keyword - 4 ###")
for letter in mystring:
    # if the letter is 'a' then skip that letter and print the rest.
    if letter == 'a':
        continue
    print (letter)

# Test 5a - break keyword
mystring = 'Sammy'
print("### Program to show 'break' keyword - 5a ###")
for letter in mystring:
    # when the letter is 'a' then break and stop the loop.
    if letter == 'a':
        break
    print (letter)

# Test 5b - break keyword
x = 0
print("### Program to show 'break' keyword - 5b ###")
while x < 5:
    # when x is equal to 2, then break and stop the loop.
    if x == 2:
        break
    print (x)
    x += 1