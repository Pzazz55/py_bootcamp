import re

text = "The agent's phone number is 408-555-1234, Call soon!"
str = "my phone once, my phone twice, my phone trice"

#TEST 1
print("\n ##### Searching a WORD in the SENTENCE - Approach 1: ##### ")
print('phone' in text)

#TEST 2
print("\n ##### Searching a WORD in the SENTENCE - Approach 2: ##### ")
patter = 'phone'
match = re.search(patter, text) #Only returns the first occurrence of the object
print(re.search(patter, text)) #Returns the matched object location (12, 17).
print("Match Span", match.span())
print("Match Start", match.start())
print("Match End", match.end())

#TEST 3
print("\n ##### Searching a WORD in the SENTENCE: ##### ")
patter = "NOT IN TEXT"
re.search(patter, text)
print(re.search(patter, text)) #Returns 'None' as there is no match available.

#TEST 4
print("\n ##### Searching all the occurrences of the WORD is a given SENTENCE: ##### ")
patter = 'phone'
matches = re.findall(patter, str) #Returns all the occurrence of the object in a List
# print(re.findall(patter, str))
print(matches)
print("Occurrences: ", len(matches))

print("\nIterating using the re.finditer :-")
for match in re.finditer(patter, str): #can be used as an iterator
    print(match)
    print(match.span())
    print(match.group()) #returns the actual text

print("\nIterating using the re.findall :-")
for match in re.findall(patter, str): #can be used as an iterator
    print(match)