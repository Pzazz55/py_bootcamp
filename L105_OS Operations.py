import os

print(os.getcwd())      # to get the current working directory.
print(os.listdir())     # listing the files in any directory.

print(os.listdir('C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya'))

# creating a file and writing into it
f = open('practise.txt', 'w+')
f.write('This is a test string')
f.close()