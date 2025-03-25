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

#Writing into a CSV file
file_to_output = open('D:\\Aryabhat\\ScriptPython\\_files\\to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',') #the delimiter can be any symbol - comma(,) semicolun (;) tab(\t)

#Writting a Single Row into the CSV file
csv_writer.writerow(['a', 'b', 'c'])

#Writting Multiple Rows into the CSV file
csv_writer.writerows([['1', '2', '3'], ['apple', 'ball', 'cat'], ['mango', '1', 'cup']])

#Close the File
file_to_output.close()

#Appending the CSV file
file_to_output = open('D:\\Aryabhat\\ScriptPython\\_files\\to_save_file.csv', mode='a', newline='') #a - append
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a_append', 'b_append', 'c_append'])
csv_writer.writerows([['10', '20', '30'], ['apple_append', 'ball_append', 'cat_append']])
file_to_output.close()