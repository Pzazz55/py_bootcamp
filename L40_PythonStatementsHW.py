#Test - 1
#Use for, .split(), and if to create a statement that will point out words that start with 's'.
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    #print(word)
    if word[0].lower() == 's':
        print(word)

#Test - 2
#Use range() to print all the even numbers from 0 to 10
print("The list of even numbers from 0 to 10: ")
#Approach - 1
mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)
#Approach - 2
print(list(range(0, 11, 2)))
#Approach - 3
for num in range(0, 11, 2):
    print(num)

#Test - 3
#Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
#Approach - 1
print([x for x in range(3, 50, 3)])
#Approach - 2
print([x for x in range(1, 51) if x % 3 == 0])

#Test - 4
#Go through the below string and if the length of a word is even print "even" !
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    if len(word) % 2 == 0:
        print(word+' is Even !')
    else:
        print(word)

#Test - 5
#Write a program that prints the integers from 1 to 100, But for multiples of three print "Fizz"
#instead of the number, and for the multiples of five print "Buzz". For number which are multiples
#of both three and five print "FizzBuzz".
mylist = list(range(1, 101))
#print(mylist)
for num in mylist:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

#Test - 6
#Use List Comprehensions to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in the string'
print([x[0] for x in st.split()])