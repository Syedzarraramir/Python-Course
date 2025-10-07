#thislist = ["apple" , "banana" , "grapes"]
#i = 0
#while i < len(thislist):
#    print(thislist[i])
#    i = i + 1
#list2 = thislist
#[print(x) for x in thislist]



'''fruits = ["apple" , "banana" , "mango" , "grapes" , "kiwi"]
newlist = [x for x in fruits if "m" in x]
print(newlist) '''

 # for x in fruits:
 #  if "m" in x:
 #      newlist.append(x)
 #       print(newlist)

'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)'''

"""thistuple = ("orange", "mango", "kiwi", "pineapple")
print(thistuple[-1])"""

"""x = ("Apple", "Orange", "Mango", "Pineapple", "Banana")
y = list(x)
y[1] = "Banana"
print(x)
x = tuple(y)
print(x)"""


"""tuple = ("orange", "mango", "kiwi", "pineapple", "banana")
(green, *yellow, red) = tuple
print(green)
print(yellow)
print(red)"""


"""looptuple = ("orange", "mango", "kiwi", "pineapple")
for x in looptuple:
    print(x)
print(len(looptuple))
y = list(looptuple)
del y[0:2]
print(y)
looptuple = tuple(y)
print(looptuple)
"""
"""looptuple = ("orange", "mango", "kiwi", "pineapple")
for x in range(len(looptuple)):
    print(x)"""

"""tuple1 = ("a" , "b" , "c")
tuple2 = 1 , 2 , 3
print(tuple1)
print(tuple2)
tuple3 = tuple1 + tuple2
print(tuple3)"""


"""tuple = ("orange", "mango", "kiwi", "pineapple")
multiplytuple = tuple * 2
print(multiplytuple)"""

"""
thiset = {"apple","banana","orange","mango","kiwi","pineapple"}
thislist = ("boys" , "girls")
print(thiset)
print(thislist)
thiset.update(thislist)
print(thiset)"""
"""
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))

for x in thisdict.items():
    print(x)



myfamily = [
    {
        "Name": "Ali",
        "Age": 19
    },
    {
        "Name": "Alex",
        "Age": 19
    },
    {
        "Name": "Bob",
        "Age": 19
    }
]

for person in myfamily:
    print(person)

for personName in myfamily:
    print(personName["Name"])
    """

"""a = 22
b = 21
if a > b:
    print("a is greater than b")
    if a > 10:
        print("a is greater than 10")
    else:
        print("a is less than 10")"""

"""day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")"""



"""i = 1
while i < 6:
    print(i)
    i = i + 1"""

"""j = 1
while j < 6:
    print(j)
    if(j == 3):
        break
    j = j + 1"""

"""i = 0
while i <= 6:
    i = i + 1
    if i == 3:
        continue
    print(i)"""


"""i = 0
while i <= 6:
    print(i)
    i = i + 1
else:
    print("i is no longer less than 6")"""


"""for x in range(2 , 30 , 6 ):
    print(x)"""


"""colors = ["red", "blue", "green", "yellow", "purple"]
fruits = ["apple", "banana", "mango", "pineapple"]
for x in fruits:
    for y in colors:
        print(x,y)"""

"""for x in [1,2,3,4,5]:
    pass"""