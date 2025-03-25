import PyPDF2
#import regular expression to search the phone number pattern
import re 

f = open('D:\\Aryabhat\\ScriptPython\\_files\\Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfReader(f)

# print(len(pdf.pages))

all_text = ''
for n in range(len(pdf.pages)):
    page =  pdf.pages[n]
    page_text = page.extract_text()

    all_text = all_text+' '+page_text

pattern = r'\d{3}.\d{3}.\d{4}'
# print(all_text)

print(re.findall(pattern, all_text))
for match in re.finditer(pattern, all_text):
    print(match)