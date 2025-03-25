'''
**********************************************************************************************************
Working with Images - Lesson 125 to 128
**********************************************************************************************************
The below script demonstrates -
- working with Images using the pillow library => install pillow library "pip install pillow"
- show how to open and save image files and interact with images.
**********************************************************************************************************
Notes -
- Pillow is a fork of the PIL (Python Imaging Library)
- Official Documentation: https://pillow.readthedocs.io/en/stable/ 
**********************************************************************************************************
'''

from PIL import Image

mac = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\example.jpg')
print("The type of the Image File ::", type(mac))
#opens the image in a seperate window
# mac.show() 
print("The size of the Image (example.jpg) is ::", mac.size)
print("The filename of the Image (example.jpg) is ::", mac.filename)
print("The format of the Image (example.jpg) is ::", mac.format_description)

############## Cropping Images ##############
#Crop the Image - 1
cropped_image = mac.crop((0, 0, 100, 100))
cropped_image.show()

#Crop the Image - 2
xaxis = (1993/2) - 200
width = (1993/2) + 200
yaxis = 800
height = 1257
mac.crop((xaxis, yaxis, width, height)).show()

pencils = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\pencils.jpg')
print("The size of the Image (pencils.jpg) is ::", pencils.size)
#Crop the Image - 3
pencils.crop((0, 0, (1950/3), (1300/10))).show() #30% of X-Axis and 10% of Y-Axis from the top-left

#Crop the Image - 4
pencils.crop((0, (1300*9)/10, (1950/3), 1300)).show() #30% of X-Axis and 10% of Y-Axis from the bottom-left

############## Copy-Paste Images ##############
computer = mac.crop((xaxis, yaxis, width, height))
mac.paste(im = computer, box=(0, 0)) #copy-paste in the top-left corner.
mac.paste(im = computer, box=(796, 0)) #copy-paste in the top-middle.
mac.show()

############## Resize Images ##############
pencils = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\pencils.jpg')
print("The size of the Image (pencils.jpg) is ::", pencils.size)
pencils.resize((3000, 500)).show()

############## Rotate Images ##############
pencils = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\pencils.jpg')
print("The size of the Image (pencils.jpg) is ::", pencils.size)
pencils.rotate((90)).show()