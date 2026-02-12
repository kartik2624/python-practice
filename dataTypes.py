#data types
x = 10 #int -> stores whole numbers
y = 10.5 #float -> stores decimal numbers
z = 2 + 3j # complex -> stores real + imaginary numbers
s = "hello, good morning" #string(str) stores text/charecters
is_valid = True # bool -> stores true or false
list1 = [1, 2, 3, 4, 5, 5] #list -> ordered, changeable collection
tuple1 = ('green', 'red', 'blue') #ordered unchangeble collection
numbers ={1, 2, 4, 5, 6, 7} #set -> unordered collection with unique values
dictionary = {'name':'kartik', 'age':21} # dict (dictionary) -> key-value pair data
res = None # represent no value

a= 1
b=10.6
print(a, id(a)) # id -> id() is used to check whether two variables point to the same object in memory
print(b, id(b))
print(isinstance(a, (int)))  # isinstance - > checkes whether a object belongs to specific data type and support inheritance
print(isinstance(b, (int, float))) #true

print(type(b)) # type return the exact data type of an object



