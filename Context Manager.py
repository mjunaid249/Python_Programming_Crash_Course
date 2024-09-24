s = "My name is Junaid"

# with open("test.txt","w") as f:
#     f.write(s)
#
# with open("test.txt","r") as f:
#     s = f.read()
#     print(s)

with open('test.txt','a') as f:
    a = ' I am also a student'
    f.write(a)