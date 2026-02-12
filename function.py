# function definition : it is block of code that can be performed a specific task when it is called.
# Types of function:
# 1.) Built-in function:
# 2.) user-defined function

def add():
    a=12
    b=12
    c=a+b
    print(f"the sum is: {c}")
add()

#function with return type
def sub():
    a = 50
    b = 25
    return a - b

res = sub()
print(f"subtract: {res}")

#function with parameter
def multi(num1: int, num2: int ) -> int: #parameters
    return num1 * num2

n1 = 25
n2 = 10
print(multi(n1, n2)) #arguments