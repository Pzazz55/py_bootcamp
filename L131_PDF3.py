'''
**********************************************************************************************************
Working with PDF and Spreadsheets - Lesson 129 to 133
**********************************************************************************************************
The below script demonstrates :-
- grabbing the content on all the pages in the PDF
**********************************************************************************************************
'''
import PyPDF2

f = open('D:\\Aryabhat\\ScriptPython\\_files\\Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

pdf_text = []

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())

print("\nThe content of the PDF is ::\n", pdf_text)
print("\nThe content of the First Page in the PDF is ::\n", pdf_text[0])
print("\nThe content of the Second Page in the PDF is ::\n", pdf_text[1])
print("\nThe content of the Third Page in the PDF is ::\n", pdf_text[2])
print("\nThe content of the Fourth Page in the PDF is ::\n", pdf_text[3])
print("\nThe content of the Fifth Page in the PDF is ::\n", pdf_text[4])