# tuple -> is collection which is ordered and unchangeable . Allows duplicate members

mytuple = ("apple", 'banana', 'cherry')
print(mytuple, type(mytuple))
 
#Ordered -> when we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#Unchangeable -> meaning that we cannot change, add or remove items after the tuple has been created.

print(len(mytuple))

#Create Tuple with one item
tu = ("apple")
print(type(tu)) #<class 'str'>

#you have to add a comma after the item, otherwise python will not recognize it as a tuple.

tu1 = ("apple",)
print(type(tu1)) #<class 'tuple'>

# tuple items data type
tuple1 = ("abs", 34, True, 40.0, "male")
# print(tuple1)

# the tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry"))
print(type(thistuple), thistuple)

# Accesing tuple items
nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(nums[1])
print(nums[-1])
print(nums[2:7])
print(nums[-7:-2])

# Check if item exists
if 80 in nums:
    print("yes, 80 is in nums tuple")

# Update Tuples
#there is workaround. u can convert the tuple into list, change list, and covert the list back into a tuple

# adding items
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y.append("orange")
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add tuple to a tuple
tup = ("apple", "banana", "cherry")
tup1 = ("orange", "Kiwi")
tup += tup1

print(tup)

# Removing Items
# you cannot remove items in a tuple

x1 = (34,34,23,22,44,54)
y1 = list(x1)
y1.remove(34)
x1 = tuple(y1)
print(x1)

# del -< keyword can delete the tuple completely
del x1

# unpacking tuple
fruits = ("apple", "banana", "cherry","greps","watermelon", "kiwi")
# (green, yellow, red) = fruits
green, yellow, *red = fruits #using asterisk * -> assign the rest values as a list called "red":
print(green)
print(yellow)
print(red)

a, *b, c = fruits
print(a)
print(b)
print(c)
 #apple ['banana', 'cherry', 'greps','watermelon'] kiwi

 # join tuples
a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 1, 1, 1, 1)
ab = a + b
print(ab)
print(ab.count(1))