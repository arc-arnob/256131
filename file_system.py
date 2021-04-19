import os,sys
# Program to write text in file

f = open('myfile.txt','w')

str = input("Enter text: ")
f.write(str)

f.close()

# Reading text from file

f = open("myfile.txt",'r')

str = f.read()
print(str)

f.close()

# Program to store a group of text in a file

f = open("myfile.txt", 'w')

while str != "@a":
    str = input()
    if str!= "@a":
        f.write(str+"\n")
f.close()

# Reading text from file

f = open("myfile.txt",'r')

str = f.read()
print(str)

f.close()

# Program to write a file, seek and then read

f = open("myfile.txt",'a+')
while str != "@a":
    str = input()
    if str != "@a":
        f.write(str+"\n")
f.seek(0,0)

str = f.read()

print(str)
f.close()

# Check whether file exists or not

fname = input("Enter file name my man: ")
if os.path.isfile(fname):
    print("Found my man\n")
else:
    print("Nope!")
    sys.exit()