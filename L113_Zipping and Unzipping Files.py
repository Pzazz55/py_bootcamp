print("Creating files and writing content into the same...")
f = open('file_one.txt', 'w+')
f.write('FIRST FILE')
f.close()

f = open('file_two.txt', 'w+')
f.write('SECOND FILE')
f.close()

#APPROACH - 1
import zipfile

print('##### FILE COMPRESSION - 1 #####')

print("Compressing the file...")
#COMPRESSEDING TWO FILES
comp_file = zipfile.ZipFile('file_compr.zip', 'w')
comp_file.write('file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

print("Extracting the file...")
#EXTRACTING THE FILE INTO A FOLDER CALLED
zip_object = zipfile.ZipFile('file_compr.zip', 'r')
zip_object.extractall('extracted_content') #folder name is extracted_content


#APPROACH - 2
import shutil

print('##### FILE COMPRESSION - 2 (shutil) #####')

print("Zipping the file...")
#ZIPPING THE FILE
dir_to_zip = "C:/Users/Naveen.Nammi/PycharmProjects/Agasthya/Jose/extracted_content"
file_name = 'shutil_example'
shutil.make_archive(file_name, 'zip', dir_to_zip)

print("Unzipping the file...")
#UNZIPPING THE FILE
shutil.unpack_archive('shutil_example.zip', 'upzip_folder', 'zip')