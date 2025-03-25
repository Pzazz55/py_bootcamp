'''
**********************************************************************************************************
Working with Advanced Python Objects - Lesson 138 to 144
**********************************************************************************************************
The below script demonstrates 'Advanced Strings':
- capitalize, upper, lower, count, find, center, expandtabs, isalnum, isalpha, islower, isupper, 
  isspace, istitle, endswith, split, partition
**********************************************************************************************************
'''
s = 'hello world'
print("\n***** String is ::", s, '*****')

#Changing Case - Capatalize the first letter of the String
print("\nCapatalize the first letter of the String ::", s.capitalize())
#Changing Case - convert every letter of the string to Upper Case
print("\nConvert every letter of the string to Upper Case ::", s.upper() )
#Changing Case - convert every letter of the string to Lower Case
print("\nConvert every letter of the string to Lower Case ::", s.lower() )

#Counting the occurrence of a letter in the String
print("\nCounting the number of occurrences of the letter 'o' in the String ::", s.count('o'))

#Find the first occurrence of a letter in the String - returns the index
print("\nCounting the first occurrence of the letter 'o' in the String ::", s.find('o'))


#center Method - allows to place the String in the center of the provided number 
print("\nPlacing the string in the center ::", s.center(20, 'z')) #total length of String is 20.

#expandtabs Method - allows to expand the \t in between the words of the String
print("\nInserting a 'tab' between the text ::", 'hello\thi'.expandtabs())

str = 'hello'

print("\n***** String is ::", str, '*****')

#Check if all the characters in the String are Alpha-Numeric
print("\nCheck if all the characters in the String are Alpha-Numeric ::", str.isalnum())

#Check if all the characters in the String are Alphabetic
print("\nCheck if all the characters in the String are Alphabetic ::", str.isalpha())

#Check if all the characters in the String are Lower Case
print("\nCheck if all the characters in the String are Lower Case ::", str.islower())

#Check if all the characters in the String are Upper Case
print("\nCheck if all the characters iin the String are Upper Case ::", str.isupper())

#Check if all the characters in the String are White Space
print("\nCheck if all the characters in the String are White Space ::", str.isspace())

#Returns 'true' if the string is a title case and there is atleast one character in it.
print("\nCheck if the string is a title case and there is atleast one character in it ::", str.istitle())

#Check if the String ends with specific character/s
print("\nCheck if the String ends with specific character 'o' ::", str.endswith('o')) #Approach1
print("Check if the String ends with specific character 'o' ::", str[-1] == 'o') #Approach2

str1 = 'hello'
str2 = 'hello theu are wonderful'

print("\n***** String is ::", str1, '*****')
print("\n***** String is ::", str2, '*****')

#Split a String at a particular Character - seperates every occurance of the Character
print("\nSplit a String at a particular Character ::", str1.split('e'))
print("Split a String at a particular Character ::", str2.split('e'))

#Seperate a String at a particular Character - retunr the first part, seperator, the last part of the String
print("\nSeperate a String at a particular Character ::", str1.partition('e'))
print("Seperate a String at a particular Character ::", str2.partition('e'))