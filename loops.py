
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
#             one iteration of the outer loop 

"""rows=int(input('how many rows?: '))
columns=int(input('how mant columns?: '))
symbol=input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end='')
    print()"""
#loop controll statement:changes a loop execution from its normal sequence
#                       break=used to terminate the loop entirely
#                       continue=skips to the nxt iteration of the loop
#                       pass=does nothing  acts as a placeholder.

"""while True:
    name=input('Enter your name: ')
    if name!="":
        break"""


"""phone_number='123-456-7890'
for i in phone_number:
    if i =="-":
        continue
    print(i,end='')"""

for i in range(1,21):
    if i==13:
        pass
    else:
        print(i)

