a = 10
b = 20
c = 12
print(a > b > c )#false
print(10 > 20) #false

x = -2
if x:
    print("true hai bhai")

# short Hand if
if a < b : print("i am shortand if")

# if else
print("b is bigger") if a < b else print("a is bigger")

print(a < b and a < c)  #True


 ### Short Circuit
print(0 and 6) # 0
a = []
print(a and 0 and 5 and 0) # 0

print(12 or '') #12
print("" or 0) #0
print('' or None)
print(3 and 10 and None or 2) # 2

print(0 and 5 or 10 and "" or None and 7 or 3) # 3

print(([] or 0 or "") and ({} or 5) or (None and 8) or 9) # 9

print(1 and 2 and 3 or 0 and 4 or 5 and None or 6) # 3

print((3 and [] or 4) and (0 or None or 7) or (" " and 0) or 100)
#          4 and 7 or 0 or 100
#          7 or 0 100  # 7



def a():
    print("A")
    return 0

def b():
    print("B")
    return 5  

def c():
    print("C")
    return None

print(a() or b() and c() or 10) 
# 0 or (5 and None) or 10
#0 or None or 10  ### 10

#pass -> avoid getting an error when block is still empty
if a:
    pass

day = 7
match day:
    case 6 | 7:
        print("heyyyy its weekend!")
    case 1 | 2 | 3 | 4 | 5:
        print("ohhh, its weekday!")
    case _:
        print("please enter valid number(1-7)")