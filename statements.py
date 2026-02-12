# if -> executes the block of code only when the condition is true

age = 18
if age >= 18:
    print("eligible for vote")

#if-else ->executes if block when the condition is true , otherwise executes the else block (if false)
age = 16
if age >= 18:
    print("eligible of vote")
else:
    print("Not eligible")

#if-elif-else -> used to check multiple conditions sequentially
marks = 75
if marks >=90:
    print("Grade: A")
elif marks >=60:
    print("Grade: B")
elif marks >=35:
    print("Grade: C")
else:
    print("Grade: F")

#nested-if -> An if statement placed inside another if statement
bus_availble = False
seat = 0
if bus_availble:
    print("Bus is available")
    if seat >= 1:
        print("seats ate avalable")
    else:
        print("All seats are full")
else:
    print("Bus is not available")

    

