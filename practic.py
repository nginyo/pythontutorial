"""number1=float(input("Enter a number: "))

if number1>=10 and number1<=20:
    number2=float(input("enter a second number: "))
    if number2>=10 and number2<=20:
        sum=number1+number2
        if sum<=100:
            print(float(sum))
        else:
            print('thats abnormal')"""


"""def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap=True
    
    
    return leap

year = int(input())



is_leap(int(input()))"""

"""n=int(input("enter a no"))
for i in range(1,n+1):
    print(i,end='')"""

"""import random 

while True:
   
    mylist=['rock','paper','scissors']
    comp=random.choice(mylist)
    mychoice=None
    while mychoice not in mylist:
        mychoice=input('rock paper scissors: ').lower()
    if mychoice==comp:
        print('its a tie')
    elif mychoice=='paper':
        if comp=='scissors':
            print(comp,mychoice+" You win")
        if comp=='rock':
            print(comp,mychoice+" You Loose")
    elif mychoice=='rock':
        if comp=='scissors':
            print(comp,mychoice+" You win")
        if comp=='paper':
            print(comp,mychoice+" You Loose")
    elif mychoice=='scissors':
        if comp=='paper':
            print(comp,mychoice+" You win")
        if comp=='rock':
            print(comp,mychoice+" You Loose")

    play_agaim=input("Y/N :").upper()
    if play_agaim!='Y':
        break
print("Bye! ")"""



"""number_grid=[
    [1,2,3,4],
    [3,4,5,6],
    [7,8,9,10],
    [0]
    ]
listone=['number1','number2','number3','number4']
numb=1
#print(number_grid[1:3],end='')
for l in listone:
    print(l)
    for num in number_grid[numb-1]:
        print(num)
    numb+=1"""

"""mylist=[i**2 for i in range(0,10)]
print(mylist)"""

numbers=(1,20,32,4,632,12,43,21)
x=sorted(numbers)
print(x[-2])
