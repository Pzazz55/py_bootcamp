from collections import Counter
#Counter is a dictionary sub-class

myList = [1, 1, 1, 1, 1, 1, 2, 3, 1, 3, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 2, 2, 2]
print(Counter(myList))

myList = ['a', 'a', 'b', 'b', 'a', 10, 'a', 10, 10, 'b', 10, 10, 10]
print(Counter(myList))

print(Counter('aaaabbbasbaababsababbabsababsbabsabsabsbasbabs'))

sentence = "How many times each word shown up in this sentence with a word"
print(Counter(sentence.split()))
print(Counter(sentence.lower().split()))

letters = 'aaaabbbdasbaababddababbabsababsbabsabsddabsbasbabs'
c = Counter(letters)
print(c)
print(c.most_common()) #operations of a counter
print(c.most_common(2))
print(list(c))  #passing a counter to a list, to get the unique values.