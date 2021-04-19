# Lets copy image

f1 = open("images\\python programming.gif","rb")
f2 = open("images\\python_copy.gif","wb")

bytes = f1.read()

f2.write(bytes)

f1.close()
f2.close()

