
#ADVANCED NUMBERS
print("\n##### 1. The binary value of 1024 is :: #####", bin(1024))
print("##### 1. The hexadecimal value of 1024 is :: #####", hex(1024))
print("\n##### 2. The value of 5.23222 when rounded to two decimals is :: #####", round(5.23222, 2))

#ADVANCED STRINGS
s = 'hello how are you Mary, are you feeling okay?'
print("\n##### 3. Check if every letter in the String is in lower case :: #####", s.islower())
str = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print("\n##### 4. Check the number of times the letter 'w' show up in the string :: #####", str.count('w'))

#ADVANCED SETS
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print("\n##### 5. Find the elements in set1 that are not in set2 :: #####", set1.difference(set2))
print("\n##### 6. Find all the elements in both the sets :: #####", set1.union(set2))

#ADVANCED DICTIONARIES
print("\n##### 7. Create a dictionary using 'Dictionary Comprehension' #####")
d = {x:x**3 for x in range(0, 5)}
print("The dictionary created using 'Dictionary Comprehension' is ::", d)

#ADVANCED LIST
l = [1, 2, 3, 4]
print("\n##### 8. Reversing the List #####")
#Reverse the List
print("The list before reversing is ::", l)
l.reverse()
print("The list after reversing is ::", l)

l = [3, 4, 2, 5, 1]
print("\n##### 9. Sorting the List #####")
#Sorting the List
print("The list before sorting is ::", l)
l.sort()
print("The list after sorting is ::", l)