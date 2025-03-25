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

############## Color Transparency ##############
#RGBA - Red, Green, Blue, Alpha
#Value of Alpha can be between 0 to 255 - where 0 showing completely White

blue = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\blue_color.png')
red = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\red_color.jpg')

#Convert both images to RGBA (if they are not in RGBA format)
red = red.convert("RGBA")
blue = blue.convert("RGBA")

#Set the alpha channel to 0 (completely White/No Background)
blue_with_alpha_0 = blue.copy()
blue_with_alpha_0.putalpha(0)  #Set Alpha to 0 (fully transparent)
blue_with_alpha_0.show()  #Show the image with Alpha = 0

#Set the alpha channel to 125 (partially transparent - BLUE)
blue_with_alpha_125 = blue.copy()
blue_with_alpha_125.putalpha(125)  #Set Alpha to 125 (partially transparent)
blue_background = Image.new("RGBA", blue.size, (255, 255, 255, 255))
blue_background.paste(blue_with_alpha_125, (0, 0), blue_with_alpha_125)
blue_background.show()

#Set the alpha channel to 125 (partially transparent - RED)
red_with_alpha_125 = red.copy()
red_with_alpha_125.putalpha(125)  #Set Alpha to 125 (partially transparent)
red_background = Image.new("RGBA", red.size, (255, 255, 255, 255))
red_background.paste(red_with_alpha_125, (0, 0), red_with_alpha_125)
red_background.show()

############## Pasting Images ##############
#Copy-Pasting one image on top of another

blue_background.paste(im=red_background, box=(0, 0), mask=red_background) 
blue_background.save('D:\\Aryabhat\\ScriptPython\\_images\\purple.png')
purple = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\purple.png')
purple.show()

