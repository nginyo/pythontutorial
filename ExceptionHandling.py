#Exception:events detected during execution that interrupts the flow of a program.

"""numerator=int(input("Enter a number to divide: "))
denominator=int(input("enter a number to divide by:"))
result=numerator/denominator
print(result)"""

try:
    numerator=int(input("Enter a number to divide: "))
    denominator=int(input("enter a number to divide by:"))
    result=numerator/denominator
 
except ZeroDivisionError as e:
    print(e)#(optional) displays an exception that occurred.
    print("You cant divide by zero!")
except ValueError as e:
    print(e)#(optional) displays an exception that occurred.
    print("Enter Number only")
except Exception as e:
    print(e)#(optional) displays an exception that occurred.
    print('Something went wrong')
else:
    print(result)
finally:
    print('this will always execute')
