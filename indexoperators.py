#index operator []=gives acccess to a sequence element (str,list,tuples)

"""name='bro code'

#if (name[0].islower()):
#    name=name.capitalize()

first_name=name[:3].upper()
last_name=name[4:].lower()
last_character=name[-1]
print(first_name)
print(last_name)
print(last_character)"""


#string formating =optional method that gives users  more control when displaying output

# animal='cow'
# item="moon"
#print('the '+animal+' jumped over the '+item)
# print(f"The {animal} jumped over the {item}")
# print("The {} jumped over the ()".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))#positional argument
# print("The {animal} Jumped over the {item}".format(animal='cow',item='moon'))#keyword argument
#print("The {animal} Jumped over the {item}".format(animal='cow',item='moon'))#keyword argument
# text="The {} jumped over the {}"
# print(text.format(animal,item))

#string padding
name="john"

print(f"Hello my name is {name:^10}. Nice to meet you")
# print("hello, My name is {}".format(name))
#print("hello, my name is {:10}.Nice to meet you.".format(name))
#print("hello, my name is {:<10}.Nice to meet you.".format(name))
#print("hello, my name is {:>10}.Nice to meet you.".format(name))
#print("hello, my name is {:^10}.Nice to meet you.".format(name))

#format numbers
number=3.14159
number2=1000
#2 decimal places
print(f"The number pi is {number:.2f}")
print("The number pi is {:.2f}".format(number))
#insert commas
print(f"The number is {number2:,}")
print("The number is {:,}".format(number2))
#convert to binary
print(f"The number is {number2:b}")
print("The number is {:b}".format(number2))
#convert to octal
print(f"The number is {number2:o}")
print("The number is {:o}".format(number2))
#convert to Hexadecimal
print(f"The number is {number2:X}")
print("The number is {:x}".format(number2))
#exponetioal or scientific notation
print(f"The number is {number2:E}")
print("The number is {:E}".format(number2))


