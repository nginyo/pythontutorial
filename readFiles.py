try:
    with open("//home//nginyo//Desktop//project//tutorial//files//text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print('that file was not found')
