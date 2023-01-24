"""first_name='bro'
last_name="code"
full_name=first_name+ ' '+last_name
print('hello '+full_name)

age=21
age+=21
print(age)
print(type(age))


height=250.5
print('your height is: ' +str(height) + "cm")
print(type(height))

human=False
print('are you human: '+str(human))
print(type(human)) """

#multiple assignment

"""name='bro'
age=21
attractive=True"""

"""name,age,attractive='bro',21, True

print(name)
print(age)
print(attractive)"""

"""pongebob=patrick=sandy=squidward=30

print(spongebob)
print(patrick)
print(sandy)
print(squidward)"""


#string methods
"""name="John karanja"
print(len(name))
print(name.find('h'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('a'))
print(name.replace('a','o'))
print(name*3)"""

#type casting

"""x=1
y=2.0
z='3'

print(str(x)*2)
print(int(y))
print(float(z)*3)

print("X is "+str(x))
print("y is "+str(y))
print("z is "+z)"""


#user input
"""name=input("what is your name?: ")
age=int(input("how old are you? "))
height=float(input('how tall are you?: '))


print('hello '+name)
print("you are "+str(age)+" years old")
print("you are "+str(height)+"cm tall")"""

#slicing

name='john karanja'
print("firstname:"+name[:4])
print("lastname: "+name[-7:])
print("funkyname:"+name[0:-1:2])
print("reversedname "+name[::-1])

website="http://google.com"
website2='http://wikipedia.com'

slice=slice(7,-4)

print(website[slice])
print(website2[slice])