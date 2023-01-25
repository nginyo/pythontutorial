number1=float(input("Enter a number: "))

if number1>=10 and number1<=20:
    number2=float(input("enter a second number: "))
    if number2>=10 and number2<=20:
        sum=number1+number2
        if sum<=100:
            print(float(sum))
        else:
            print('thats abnormal')