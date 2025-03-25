'''
**********************************************************************************************************
Working with PDF and Spreadsheets - Lesson 129 to 133
**********************************************************************************************************
The below script demonstrates :-
- writting into a PDF file
  Extract the First Page of 'Working_Business_Proposal.pdf', and create a New File 'Some_BrandNew_Doc.pdf' 
  with this content.
**********************************************************************************************************
'''
import PyPDF2

#Adding pages to the PDF file

f = open('D:\\Aryabhat\\ScriptPython\\_files\\Working_Business_Proposal.pdf', 'rb') #rb - Read Binary
pdf_reader = PyPDF2.PdfReader(f)

#Extracting the First Page
first_page = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
# print(type(first_page))
pdf_writer.add_page(first_page)

#Creates a New File Programmatically
pdf_output = open('D:\\Aryabhat\\ScriptPython\\_files\\Some_BrandNew_Doc.pdf', 'wb') #wb - Write Binary
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()