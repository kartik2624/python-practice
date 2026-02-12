# List -> 

city = ['gadag', 'bengaluru', 'hubli', 'kolar']

# print(type(city))
print(len(city)) #4
# print(city)

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

#List manipulation

##### adding elements to the list #####
city.append('Mangalore') #Add item at last of list

city.insert(1, 'chickmanglore') #insert item at given index 

##### removing elements from list ########
city.remove('chickmanglore') # deletes based on given name element

city.pop() #deletes last element (manglore)

del city[3] # deletes based on given index

print(city)

### Nested List ####
neslist = ['gadag', ['rona', 'lakshmeshara', 'mundargi', 'shiratti','gadag', 'nargund','gajendragad']]
print(neslist)

# Accessing nested array
print(neslist[1][6]) #Gajendragad


        

