
def myfunc(name):
    print('Hello '+ name)

myfunc('Naveen')

def myfunc(value_bool):
    if value_bool:
        return('Hello')
    else:
        return('Goodbye')

x = myfunc(0)
print(x)

def myfunc(*args):
    mylist = []
    for items in args:
        if items % 2 == 0:
            mylist.append(items)
    return mylist

x = myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x)


def myfunc(*args):
    #print(args)
    mystr = ""
    i = 0
    #print(len(args[0]))
    for i in range(0, len(args[0])):
        #print(args[0][i])
        if i % 2 == 0:
            mystr += args[0][i].upper()
        else:
            mystr += args[0][i].lower()
        i += 1
    return mystr

x = myfunc('Anthropomorphism')
print(x)


def myfunc(*args):
    result = ""
    for index, letter in enumerate(*args):
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
    return result

x = myfunc('Anthropomorphism')
print(x)