import csv

#Opening the CSV File
try:
    data = open('D:\\Aryabhat\\ScriptPython\\_files\\find_the_link.csv', encoding='ISO-8859-1')
    #the encodoing = 'utf-8' cannot be used because the .cvs file contains '@' symbol (Email Addresses)
except UnicodeDecodeError:
    print("Encoding issue with ISO-8859-1, trying 'latin1' encoding.")

csv_data = csv.reader(data)
data_lines = list(csv_data)

#Approach - 1
link_str = ''
for row_num, data in enumerate(data_lines): #the trick is to use enumerate
    link_str += data[row_num]
print(link_str)

#Approach - 2
diagonal_elements = ''
num_rows = len(data_lines)
for i in range(num_rows):
    if i < len(data_lines[i]):  #check if the row has enough columns
        diagonal_elements += data_lines[i][i]
print(diagonal_elements)