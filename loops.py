#for loops -> executes a block of code repetedly until conditions fails

for i in range(1,10): #using range 
    print(i)
fruits = ['apple', 'mango', 'greyps', 'kivi', 'banana']
for fruit in fruits:
    print(fruit, end=" ")
print()

#while loop -> repeats execution until the condition becomes false
i=0
while i <= 10:
    print(i, end=" ")
    i+=1
print()

available_seats = 3
while available_seats > 0:
    print("seats are availble")
    available_seats-=1
print("seats are not available")


#Break keyword->Stops the loop immediately when a condition is met
for i in range(1,10):
    print(i, end=" ")
    if i == 4:
        break
print()

#continue keyword-> skips the current iteration and continues with the next one
for i in range(1,10):
    if i == 3:
        continue
    print(i, end=" ")
print()
