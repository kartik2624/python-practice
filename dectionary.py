# Dictionary -> is collection which is ordered and changeable . No duplicate members.
#Dictionaries are used to store data values in key:value pairs.

mydict = {
    "name" : "kartik",
    "age" : 21,
    "class" : "Python",
}

print(mydict)
print(len(mydict), type(mydict))
print(mydict['age'])
x = mydict['name']
print(x)
keyss = mydict.keys()
print(keyss)

mydict["phone"] = 8884439315

print(keyss)

val = mydict.values()
print(val)

mydict["age"] = 22
print(val)

mydict["hasCar"] = False

print(val)

item = mydict.items()
print(item)

mydict["hasBike"] = True

print(item)

# check if key exist
if 'age' in mydict:
    print("found")

#Update method:  multiple items can update or add
mydict.update({"course" : "Full Stack", "Location": "Gadag"})

print(mydict)

## Removing Dictionary Items
# i.) pop()
mydict.pop("hasCar")

# ii) popitem() -> method removes last inserted item
mydict.popitem()

#iii) del
del mydict["hasBike"]

#and
#del mydict #deletes the dictionary

# iv) clear() method empties the dictionary.
#mydict.clear()  #{}

print(mydict)

# loop through Dictionary

# for k in mydict:
#     print(k)
    # print(mydict[k])

for v in mydict.values():
    print(v)

for k, v in mydict.items():
    print(k,':', v)

# copy dictionary
dictionary = mydict.copy()

dictionary1 = dict(mydict)


# Nested dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)
    
    for x, v in obj.items():
        print(x,':',v)

arr = ['a', 'b', 'c', 'd']
x1 = dict.fromkeys(arr)
print(x1)