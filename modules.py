import random

# x=random.randint(1,6)
# y=random.random() #generates a floating point number
# print(y)
# print(x)
myList=['rock','paper','scissors']
z=random.choice(myList)
print(z)

cards=[1,2,3,4,5,6,7,8,9,'J',"Q","K","A"]
random.shuffle(cards)
print(cards)