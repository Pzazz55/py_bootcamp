'''
os.unlink() - delete a file at the path provided.
os.rmdir() - deletes a folder (folder must be empty) at the path your provided.
shutil.rmtree(path) - removes all the files and folders contained in the path

All the above methods are dangerous and cannot be reversed/recovered. Instead, we will use the
send2trash module (that is a safer alternative) and sends the deleted files to the trash bin instead
of permanent removal.

pip install send2trash  --at the command line.
'''

import os
import shutil
import send2trash

#Creating a file in the present working directory and writing into it.
f = open('practise.txt', 'w+')
f.write('This is a test string')
f.close()

shutil.move('C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya\\Jose\\practise.txt',
            'C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya')

#list all the files/folders under the mentioned path
print(os.listdir('C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya'))

#delete the mentioned files into trash
send2trash.send2trash('C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya\\practise.txt')
print(os.listdir('C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya'))

#list all the folders, sub-folder and files under the mentioned path
file_path = 'C:\\Users\\Naveen.Nammi\\PycharmProjects\\Agasthya'
# for dir, subdir, file in os.walk(os.getcwd()):
for dir, subdir, files in os.walk(file_path):
#os.walk() is going to make a tree and walk each and every single file in the file_path location.
    print(f"Currently looking at {dir}")
    print('\n')
    print(f"The sub-folders are - ")

    for sub_dir in subdir:
        print(f"\t Subfolder Name: {sub_dir}")
        print('\n')
        print(f"The files are -")

        for f in files:
            print(f"\t\t File Name: {f}")
            print('\n')