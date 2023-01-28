import os

#path ="//home//nginyo//Desktop//project//tutorial//files//file.txt"
#path ="//home//nginyo//Desktop//project//tutorial//files"


"""if os.path.exists(path):
    print('that location exists')
else:
    print("that location doesnt exists")"""

"""if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file:")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("that location doesn't exist")"""

"""if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file:")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("that location doesn't exist")"""

"""try:
    with open("//home//nginyo//Desktop//project//tutorial//files//text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print('that file was not found')"""

#writing files
"""text="this has been\n overwirtten"

with open('test.txt','w')as file:
    file.write(text)
"""
#append a a text to file
"""text="\nthis line was added\n"

with open('test.txt','a')as file:
    file.write(text)"""

#copying files
#copyfile()=copies content of a file
#copy()=copyfile+permission mode +destination can be a directory
#copy2()=copy()+copies metadata(file creation and modification times)

"""import shutil

shutil.copyfile('test.txt','copy2.txt')#src and destination
shutil.copy('test.txt','copy1.txt')
shutil.copyfile('test.txt','copy3.txt')"""

#moving file in python
#moving a file
"""import os 
source="test.txt"
destination="//home//nginyo//Desktop//project//tutorial//files//test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+"was moved")
except FileNotFoundError:
    print(source+ "was not found")"""
#moving a folder
"""import os 
source="folder"
destination="//home//nginyo//Desktop//project//tutorial//files//folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+"was moved")
except FileNotFoundError:
    print(source+ "was not found")"""


#Deleting files
"""import os

path='new.txt'
try:
    os.remove(path)
except FileNotFoundError:
    print("that file was not found")"""

#removing a directory
import os
import shutil
path='folder'

try:
    os.rmdir(path)#deletes empty directory
    #shutil.rmtree(path)#deletes a folder containing files 
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('you do not have permisiion to delete that')
else:
    print(path+'was deleted')
