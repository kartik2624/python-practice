#String -> a String is sequence of characters enclosed in quotes.

name = "Kartik"
email = "kartikkatwa3@gmail.com"
course = " python full stack development  "

# string Operations
print(len(name)) # length -> len(str_name)

print(name[0]) #indexing -> name[0] == k

print(name[1:]) #slicing -> name[1:] == artik

print('name:' + name + "email: " + email) #Concatenation (+)

print('Ha'*3) #Repetition (*)


#string Methods


print(name.upper()) #UpperCase
print(name.lower()) #LowerCase

print(email.capitalize()) #Capitalize -> first letter converts into uppercase
print(course.title()) # every word starts with capital letter

print(course.strip()) #removes unwanted spaces from input froms

ls = course.split() #to convert string to list (used in data parsing)
print(ls)

print(" ".join(ls)) #to convert list into string

print(course.replace('python', 'MERN')) #Data cleaning

print(course.find("python")) #return index of first given letter if not found then return -1

print(course.index("e")) #if not found raises valueError: substring not found

file = "data.csv"
print(file.endswith(".csv")) #return true
print(file.startswith("d")) #reutn true

num = "2343"
char = "hellomorning"
varchar = "kartik242635"
print(num.isdigit()) #checks only numbers
print(char.isalpha()) #only letters no space no special chars and no numbers
print(varchar.isalnum()) #only numbers and letters no specail chars and space.

print(course.swapcase()) #kArTiK it converts small letters to capital and capital to small letters on given string

print(num.zfill(10)) # adds zero to fill given length of numbers

print(email.partition("@")) # split into 3 parts



