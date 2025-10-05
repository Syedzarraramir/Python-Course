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



