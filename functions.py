#Function= is a block of code which is executed only when its called/

"""def hello(fname,lname,age):
    print('hello '+fname +" "+lname)
    print('you are ' +str(age)+ ' years old')
    print('have a nice day')


#myname="Bro"
hello('john','karanja',21)"""


#return statement = Functions sends python values/objects back to the caller.
#                   this values/objects are known as the function return value.
# the same way a caller gives argument to a function.a function also gives result back to the caller
# which are called return values.

#def multiply(number1,number2):
  #  result=number1*number2
   # return result

#print(multiply(6,8))
#x=multiply(6,8)
#print(x)

"""def multiply(number1,number2):
    return number1*number2

x=multiply(6,8)
print(x)"""

#Keyword Arguments: This are arguments that are preceded by an identifier when we pass them to a function
#                    The order of the argument doesnt matter unlike positional arguments
#                    Python knows the names of the arguments that our function receives

"""def hello(first,middle,last):
    print('hello '+first+' '+middle+' '+last)
#positional arg:order does matter
hello('John','Karanja','nginyo')
hello('nginyo','karanja','john')

#keyword arg:order doesnt matter
hello(last='nginyo',first='john',middle='karanja')"""


#Nested function calls:fuction calls inside other function calls
#                       inside function calls are resolved first
#                       returned value is used as argument for the nxt outer function

#num=input('Enter a whole positive number')
#num=float(num)
#num=abs(num)
#num=round(num)
#print(num)

#print(round(abs(float(input('Enter a whole number')))))


#Scope: the region that a variable is recognised
#       A variable is only available from inside a region its created.
#       A global and locally scoped versions of a variable can be created

#local variable
"""def display_name():
    name='Code' #local var(available only inside the function)
    print(name)
print(name)"""

"""name="Bro" #global scope(available inside and outside function)

def display_name():
    #name='Code' #local var(available only inside the function)
    print(name)


print(display_name())
print(name)"""


# *args:parameter that will pack all arguments into a tuple.positional
#    useful that a function can accept a varying amount of arguments

"""def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,4,5,6))


def add(*stuff):
    sum=0
    for i in stuff:
        sum+=i
    return sum
print(add(1,2,3,4,5,6))

def add(*stuff):
    sum=0
    stuff=list(stuff) #cast a tuple into a list then change one of its value
    stuff[0]=10
    for i in stuff:
        sum+=i
    return sum
print(add(1,2,3,4,5,6))"""

"""def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(20,20,40,50))"""

# **kwargs=parameter that parks all arguments into a dictionary ,keyword arguments
#          useful so that a function can accept a varying amount of keyword arguments