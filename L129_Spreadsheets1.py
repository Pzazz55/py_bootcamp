'''
**********************************************************************************************************
Working with PDF and Spreadsheets - Lesson 129 to 133
**********************************************************************************************************
The below script demonstrates :-
- working with built-in CSV module for Python, that allow us to grab columns, rows, and values from a 
  .csv file
**********************************************************************************************************
Notes -
- CSV stands for Comma Seperated Variables, and is a very common o/p for a spreadsheet program.
- CSV file only contains the raw data from the spreadsheet. Things like formulas, images, and macros 
  can not be within a .csv file
- Other libraries to consider are -
    - Pandas (works with .csv, Excel, SQL files)
    - Openpyxl (designed for Excel files - supports Excel specific functionality) - python-excel.org 
      tracks various other Excel based Python libraries.
    - Google Sheets Python API (allows directly make changes to spreadsheet hosted online)
- The common factor between all of these spreadsheet programs is that they can always export to .csv
**********************************************************************************************************
'''
import csv

#Opening the CSV File
data = open('D:\\Aryabhat\\ScriptPython\\_files\\example.csv', encoding='utf-8')
#throws the below UnicodeDecodeError - because the .cvs file contains '@' symbol (Email Addresses) - so, the encoding = 'utf-8'
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 1810: character maps to <undefined>

#Converting the file into CSV data - csv. reader
csv_data = csv.reader(data)

#Reformating into a Python object list of lists
data_lines = list(csv_data)

print(data_lines) #this is a list of lists
print("\nThe length of the CSV file (rows) is ::\n", len(data_lines))
print("\nThe columns in the CSV file are ::\n", data_lines[0]) #shows the column names

print("\nThe top 5 lines in the CSV file are ::")
for line in data_lines[:5]:
    print(line)

print("\nExtract the specific line of the CSV file - 10th line ::")
print(data_lines[10])

print("\nExtract the specific value in the line of the CSV file - Email Address ::")
print(data_lines[10][3])

print("\nExtract the entire column of the CSV file - Emails ::")
all_emails = []
n = len(data_lines)
# for lines in data_lines[1:len(data_lines)]:
for line in data_lines[1:n]:
    all_emails.append(line[3])
print(all_emails)

print("\nExtract the First & Last Name columns and combining the same ::")
full_name = []
for line in data_lines[1:]:
    full_name.append(line[1] +' '+ line[2])
print(full_name)