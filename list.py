# List -> is collection which is ordered and changeable. Allows duplicate members

city = ['gadag', 'bengaluru', 'hubli', 'kolar']

# print(type(city))
print(len(city)) #4
# print(city)
# print(city[1:7]) #If end index is bigger than list size, Python will stop at the last element (no error)

#accessing elements one by one 
# print(city[0])
# print(city[1])
# print(city[2])
# print(city[3])

# Accessing by loop
# for el in city:
#     print(el ,end=" ")

#  modifying
city[3] = 'Dharwad'
# print(city)
city[2:5] = ["Hubli", "Koppal", "Mysore"]
# print(city)
city[2:3] = ["Belagavi", "Ballari", "Hasana"]
# print(city)

#List manipulation

##### adding elements to the list #####
city.append('Mangalore') #Add item at last of list
# print(city)
city.insert(1, 'chickmanglore')
city2 = ['Gulburga', 'Bagalgote', 'Haveri'] #insert item at given index 
city.extend(city2)
# print(city)
##### removing elements from list ########
city.remove('chickmanglore') # deletes based on given name element

city.pop() #deletes last element (manglore)

del city[3] # deletes based on given index
# del city2

city2.clear() #meothd empties the list
# print(city2)

# print(city)

# if 'gadag' in city:
#     print("yes, \"gadag\" is in the city list")

#Loop though list
# for x in city:
#     print(x)
# for i in range(len(city)):
#     print(city[i])

#List Comprehension -> used to create a new list
# [print(x) for x in city]

#best practice for list comprehension
nums = [41,25,5,44,24,16,58,36,32,25,75,15]
evenNums = []
evenNums = [x for x in nums if x % 2 == 0]
# print(evenNums)

# newcity = [x if x == 'gadag' else 'Gadag' for x in city]
# print(newcity)


#sorting a list
# city.sort()
# print(city)

city.sort(key=str.lower, reverse = True) #case sensitive
# print(city)

print(city.reverse()) # none -> reverse() returns none , it modifies the list
nums.reverse()
# print(nums)

#copy a list  3 ways to copy a list
vowels = ['a', 'e', 'i', 'o', 'u']
# copied_vwls = vowels.copy()
# copied_vwls = list(vowels)
copied_vwls = vowels[:]
# print(copied_vwls)



#join Two Lists
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

total = num1 + num2  # + operator

# print(total)


#by looping
# for x in num2:
#     num1.append(x)
# print(num1)

# extend method

num1.extend(num2)
print(num1)

















### Nested List ####


neslist = ['gadag', ['rona', 'lakshmeshara', 'mundargi', 'shiratti','gadag', 'nargund','gajendragad']]
# print(neslist)

# Accessing nested array
# print(neslist[1][6]) #Gajendragad


        

