#oparators

# Arithmetic Oparators (+ - * / % // **)
# Assignment oparators (+= -= *= /=)
# Comparison oparators (== < > <= >= !=)
# Logical (and or not)
# identity (is  is not)
# membership (in  not in)
# Bitwise  (&)

num1 = 14
num2 = 5

# 1.) Arithmetic Oparator
#addition
print("addition:", num1 + num2)
#substraction
print("sub:", num1 - num2)
#multiplication
print("multi:", num1 * num2)
#modulus
print("modulus:", num1 % num2)
#division
print("divison:", num1 / num2)
#floor division
print("floor division:", num1 // num2)
#expondation (powerOf)
print("expondation:", num2 ** 2)

#2.) Comparison oparators
# print(num1 == num2) #false
# print(num1 !=  num2) #true
# print(num1 > num2) #true
# print(num1 < num2) #false
# print(num1 >= num2) #true
# print(num1 <= num2) #false

#3.) Assignment Oparator
balance = 100 #Assignment oparator (=)
balance += 20 #Add and Assign(+=)
balance -= 10 #Subtract and Assign(-=)
balance *= 2 #Multiply and Assign(*=)
balance /= 3 #division and Assign(/=)
balance //= 2 #floor division and assign(//=)
balance **= 2 #exponent and assign (**=)
print(balance) #1296
balance %= 2 #modulus and Assign(%=)

# 4.) Logical Oparator

# i) Logical and : Returnn true only if both conditions are true..
user1 = True
user2 = True
print(user1 and user2) #True

# ii) Logical or : Returns true if at least one condition is true.
user2 = False
print(user1 or user2) #true

# iii) Logical not : Reverse the boolean value of a condition
print(not user2) #false

# 5.)identity Operator
# i) is ->Return true if both variable point to he same object in memory.
a = [1,2,3]
b = a
print(a is b) #true

# ii) is not ->return true if variable point to different object, even if value are the same
print(a is not b) #false

# 6.) Membership Operator
# i) in -> returns true if the value exists in a sequence.
items = ['pen', 'book', 'notebook']
print("pen" in items) #true

# ii) not in -> return true if the value does not exist in sequence.
print("pencil" not in items) #true
print("pen" not in items) #false

# 7.) bitwise operator
print(5 & 6)






