from collections import defaultdict

#The below is an example of normal dictionary.
d = {'a': 10}
print(d)
print(d['a'])
#print(d['WRONG']) #it throws a KeyError.

#The below is an example of default dictionary.
d = defaultdict(lambda: 0)
d['correct'] = 100
d['WRONG KEY']
d['WRONG KEY']
d['incorrect'] = 50
d['ANOTHER WRONG KEY']
print(d.items())