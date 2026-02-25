# sets -> is collection which is unordered, unchangeable and unindexed. No duplicate members.
#set items are unchangeable, but you can remove and add items whenever you like.

myset = {"apple", "banana", "cherry"}
print(myset)

#the values true and 1 are considered the same value in set. and similar to false and 0
myset1 = {True, 1, 0, False}
print(myset1)

print(len(myset1))
print(type(myset)) #<class 'set'>

# use set constructor
myset2 = set(("apple", "banana", "cherry"))
# print(myset2)

# loop through the set
# for x in myset:
#     print(x)

print("banana" in myset) # true 

### Add Items -> add(). method
myset.add("orange")
# print(myset)

### Add Sets -> update(). method to add items from another set or any iterable (list, or tuple)
myset.update(myset1)

print(myset)

mylist = [1, 3, 5, 7, 9, 11]

myset.update(mylist)
myset.update((6, "hello", "morning"))

print(myset)

## Remove Item
# remove(), or discard(). method

myset.remove(6) # if item does not exit, raise an ERROR.

myset.discard('hello') #if item does not exit, will NOT raise an ERROR.
print(myset)

print(mylist.pop()) # return removed item, it removes a random item

myset2.clear()
print(myset2) #set()

del myset2  # delete the set completely

# Join Sets
nums1 = {2, 4, 5, 6, 7, 8, 0}
nums2 = {1, 2, 3, 4, 5, 6, 9, 10}

#union() and update() -> joins all items from both sets

# union() // | operator return a new set with all items frrom both sets

uni = nums1.union(nums2)
print(uni)

 # Use | to join two sets
uni1 = nums2 | nums1
print(uni1)

### join multiple sets
nums3 = {10,11,12,13,15, 2, 4, 5}
# multi_set = nums1 | nums2 | nums3
multi_set = nums1.union(nums2, nums3)
print(multi_set)

# the union() method allow u to join a set with other data types, like kist or tuples

x = {'a', 'b', 'c'}
y = (1, 2, 3)
z = x.union(y)
print(z)
# the | operator only allows u to join sets with sets

### Intersection() // &
#intersection().method will return anew set, that only contains the items that are present in both sets.

# intsec = nums1.intersection(nums2)
intsec = nums1 & nums2
print(intsec) # return duplicate items

#intersection_update().
#it will change the original set instead of returning a new set.
# nums1.intersection_update(nums2)
# print(nums1)


### difference() or '-'.
#return new set, that will contai only the items from the first set that are not present in the other set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)
set3 = set2 - set1

print("hello", set3)


#### Symmetric Differences
# the symmetric difference(). method will keep only the elements that are NOT present in both sets.

items1 = {"apple", "banana", "cherry"}
items2 = {"google", "microsoft", "apple"}

items3 = items1.symmetric_difference(items2)
print("symmetric difference:", items3)





