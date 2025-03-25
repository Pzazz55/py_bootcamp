from PIL import Image

#snippet to open an image from a location
word_img = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\word_matrix.png')
mask_img = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\mask.png')

#snippet to find the size of an image, and resize it
print("The size of the Image (example.jpg) is ::", word_img.size)
print("The size of the Image (example.jpg) is ::", mask_img.size)
mask_img = mask_img.resize((1015, 559))

#validation statements
# Image.open('D:\\Aryabhat\\ScriptPython\\_images\\new_mask.png').show()
# print("The size of the Image (example.jpg) is ::", word_img.size)
# print("The size of the Image (example.jpg) is ::", new_mask.size)

#snippet to translucent an image - 'mask.png'
mask_125 = mask_img.copy()
mask_125.putalpha(125)  #Set Alpha to 125 (partially transparent)
mask_background = Image.new("RGBA", mask_img.size, (255, 255, 255, 255))
mask_background.paste(mask_125, (0, 0), mask_125)

#validation statements
# mask_background.show()

#snippet to copy-paste an image on top of another image, and saving the new image to a location
word_img.paste(im=mask_background, box=(0, 0), mask=mask_background) 
word_img.save('D:\\Aryabhat\\ScriptPython\\_images\\overlap.png')
overlap = Image.open('D:\\Aryabhat\\ScriptPython\\_images\\overlap.png')
overlap.show()