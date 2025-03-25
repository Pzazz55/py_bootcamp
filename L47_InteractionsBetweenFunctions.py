'''
Interactions between Functions

*** Three Cup Monte - Game ***
'''

# Test 1 - Shuffling a list in random in Python.
print("### Program to shuffle a list in random - 1 ###")
example = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from random import shuffle
print(f'The list before shuffling is {example}.')
shuffle(example)
print(f'The list after shuffling is {example}.')

# Test 2 - Write a program to create a Three Cup Monte Game.
print("### Three Cup Monte Game - 2 ###")

def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)

def player_guess():
    guess = ''
    while guess not in [0, 1, 2]:
        guess = int(input("Pick a Number 0, 1, or 2: "))
    return guess

def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print("Correct")
    else:
        print("Wrong Guess")
        print(mylist)

#INITAL LIST
from random import shuffle
mylist = ['', '0', '']

#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list, guess)
