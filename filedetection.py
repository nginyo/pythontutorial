import os

#path ="//home//nginyo//Desktop//project//tutorial//files//file.txt"
path ="//home//nginyo//Desktop//project//tutorial//files"


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

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file:")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("that location doesn't exist")