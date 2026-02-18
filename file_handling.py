# f = open("demofile.txt", 'r')
# print(f.read())
# print(f.read())
# f.close()

# f.write("hello, good morning ")
# f.write("Welcome to python coding class ")
# f.write("python full stack development ")

# with open("demofile.txt") as f:
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readlines())
    # for x in f: # looping through the file line by line
        # print(x)

# with open("demofile.txt", 'a') as f:
#     f.write("\nthis text has been appended")
#     f.write("\nanother line append")

# with open("demofile.txt", 'r') as f:
#     print(f.read())

# with open("demofile.txt", 'w') as f:   #'w'-> will delete existing content / orerwrite the existing constent with new given content
#     f.write("Woops! I have deleted the content!")

# with open("demofile.txt") as f:
#     print(f.read())

# f = open("myfile.txt", 'x')
# with open("myfile.txt", 'a') as f:
    # f.write("creating a file from python file\n")
    # f.write("appending few lines for better understanding\n")
    # f.write("the 'w' method will overwrite the entire file\n")
    # f.write("'x'-Create - will create a file, returns an error if the file exists\n")
    # f.write("'a'-Append - will append to the end of the file\n")

with open("myfile.txt") as f:
    print(f.read())

f = open("emptyfile.txt", "x")



