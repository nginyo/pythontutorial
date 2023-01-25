#Lists:used to store multiple items in a single variable

"""food=['pizza','humberger','hotdog','spaghetti']

food[0]='sushi'
print(food)
print(food[3])

#food.append('ice cream')
#food.remove('humberger')
#food.pop()#removes last item
#food.insert(0,'cake')
#food.sort()#sorts alphabetically
#food.clear()#removes all the elemnent in the list

for x in food:
    print(x )"""

#2d list/multi dimensional lists: a list of list

"""drinks=["coffee",'soda','tea']
dinner=['pizza','humberger','hotdog']
dessert=['cake','icecream']

food=[drinks,dinner,dessert]
#print(food)
print(food[1][2])"""

#Tuples=collection which is ordered and unchangeble used to group
#        together related data

"""student=("bro",21,'male')

print(student.count('bro'))
print(student.index('male'))

for x in student:
    print(x)

if 'bro' in student:
    print('bro is here: ')"""


#set = collection which is unorderd,unindexed. no duplicate values

"""utensils={'fork','spoon','knife','knife','knife'}
dishes={'bowl','plate','cup','knife'}
#utensils.add('napkin')
#utensils.remove('fork')
#utensils.clear()
#utensils.update(dishes)
#dinnertable = utensils.union(dishes)#joins two sets together

for x in utensils:
    print(x)

for x in dinnertable:
    print(x)

#print(utensils.difference(dishes))    #prints items which are in utensils but not in dishes

print(utensils.intersection(dishes)) #prints items that are in utensils and in dishes"""

#dictionary:A changeable,unordered collection of unique key:value pairs
#            Fast because they use hashing,allow us to access a value quickly

"""capitals={"USA":"Washington DC",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()
#print(capitals['India'])
#print(capitals.get('Germany'))

#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)"""
