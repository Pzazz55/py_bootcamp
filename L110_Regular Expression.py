import re

text = "The agent's phone number is 408-555-1234, Call soon!"

phone = re.search('408-555-1234', text)
print(phone)

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())

#using a quantifier to indicate the repetition of the same character
print("\nUsing a quantifier to indicate the repetition of the same character.")
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())

phone_patter = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_patter, text)
results.group()
print("Show all the Groups: ", results.group())
print("Show the 1st Sub-Group: ", results.group(1))
print("Show the 2nd Sub-Group: ", results.group(2))
print("Show the 3rd Sub-Group: ", results.group(3))