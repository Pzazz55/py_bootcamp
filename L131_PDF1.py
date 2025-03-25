'''
**********************************************************************************************************
Working with PDF and Spreadsheets - Lesson 129 to 133
**********************************************************************************************************
The below script demonstrates :-
- install PyPDF2 "pip install PyPDF2"
- working with PDFs using Python: allow us to make additions to PDF's such as images, tables, format 
  adjustments can also render a PDF unreadable by Python.
**********************************************************************************************************
Notes -
- PDF stands for Portable Document Format, and was developed by Adobe in 1990's.
- While PDF's share the same extension, and can be viewed in PDF reader, many PDF's are not machine 
  readable by through Python.
- Since PDFs mainly encapsulate and display a fixed-layout flat document, there is no machine readable
  standard format, unlike CSV files. Meaning, the PDF's that are scanned are highly unlikely to be 
  readable by the Python.
- There are many paid PDF programs that can read and extract from these files, but here we will use the
  open-source and free PyPDF2 library.
**********************************************************************************************************
'''

import PyPDF2

#Opening the PDF File
f = open('D:\\Aryabhat\\ScriptPython\\_files\\Working_Business_Proposal.pdf', 'rb') #rb - Read Binary
pdf_reader = PyPDF2.PdfReader(f)

#Extracting the total number of pages in the PDF
print("The total pages in the PDF are ::", len(pdf_reader.pages))

#Reading the First Page of the PDF
page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(page_one_text)

f.close()

