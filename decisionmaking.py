import time
#if statements
"""age=int(input('How old are you?: '))
if age==100:
    print("You are a Centurion")
elif age>=18:
     print('you are an adult')
elif age<0:
    print('You havent been born yet.')
else:
    print('You are a child.') """


#logical operators

"""temp=int(input('What is the temperature outside? :'))
if temp>=0 and temp<=30:
    print('the temp is good today go outside')
    print('Go Outside!')
elif temp<0 or temp>30:
    print("the temperature is bad today!")
    print('stay inside')"""
#not operator

"""temp=int(input('What is the temperature outside? :'))
if not(temp>=0 and temp<=30):
    print("the temperature is bad today!")
    print('stay inside')
    
elif not(temp<0 or temp>30):
    print('the temp is good today go outside')
    print('Go Outside!')"""

#while loops: a statement that executes as long as a condition is true.
#             while loop=unlimited
"""name=''
while len(name)==0:
    name=input("Enter your name: ")
print("hello "+name)"""

"""name=None

while not name:
    name=input("Enter your name: ")
print("hello "+name)"""

#for loop: a statement that will execute its block of code a limited
#           amount of time
#         for loop:limited

#for i in range(10):#10 is ecxlusive
    #print(i)

#for i in range(50,100,2): #50 start 100 stop 2 step
#    print(i)

#for i in 'John Karanja':
#    print(i)
#timer
"""for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")"""

#Nested Loops:the inner loop will finish all of its iteration before finishing
#             obe iteration of the outer loop 

rows=int(input('how many rows?: '))
columns=int(input('how mant columns?: '))
symbol=input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end='')
    print()

