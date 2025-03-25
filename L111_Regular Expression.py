import re

print("##### Check if 'cat' is there in the string #####")
print(re.search(r'cat','The cat is here')) #check if cat is there in the string.

print("##### Check if 'dog' is there in the string #####")
print(re.search(r'dog','The cat is here'))

print("##### Check if 'cat or dog' is there in the string #####")
print(re.search(r'cat|dog','The cat is here'))

print("##### Check if 'at' is there in the string #####")
print(re.findall(r'at','The cat in the hat sat there.'))

print("##### Check if '%at' is there in the string, and print all the respective words - wild card search #####")
print(re.findall(r'.at','The cat in the hat sat there.'))

print("##### Check if '%%%at' is there in the string, and print all the respective words - wild card search #####")
print(re.findall(r'...at','The cat in the hat went splat.'))

print("##### Check if the pattern occurs in ths string #####")
print(re.findall(r'^\d', '5 is a Number')) #start with - ^
print(re.findall(r'^\d', 'The 5 is a Number'))
print(re.findall(r'\d$', 'Number is 5')) #ends with - $

print("##### Finding pattern based on the Regular Expression #####")
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern1 = r'[^\d]'
print(re.findall(pattern1, phrase))

pattern2 = r'[^\d]+'
print(re.findall(pattern2, phrase))

print("##### Finding pattern using Regular Expression - Grouping for Exclusion #####")
text_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall(r'[^!.?]+', text_phrase))
print(re.findall(r'[^!.? ]+', text_phrase)) #removing spaces to get the list of words.

clean = re.findall(r'[^!.?]+', text_phrase)
print(' '.join(clean))

print("##### Finding pattern using Regular Expression - Grouping for Inclusion #####")
text_phrase = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+'
print(re.findall(pattern, text_phrase))
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text_phrase))
pattern = r'\w+-\w+'
print(re.findall(pattern, text_phrase))

print("##### Combining the 'or' statement with other pieces of text #####")
text_one = 'Hello, would you like some catfish?'
text_two = "Hello, would you like to take a catnap?"
text_three = "Hello, have you seen this caterpillar?"
print(re.search(r'cat(fish|nap|claw)', text_one))
print(re.search(r'cat(fish|nap|claw)', text_two))
print(re.search(r'cat(fish|nap|claw)', text_three)) #returns None
print(re.search(r'cat(fish|nap|erpillar)', text_three))