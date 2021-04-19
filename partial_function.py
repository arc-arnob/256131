from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

# An important note: the default values will start replacing variables from the left. 
# The 2 will replace x. y will equal 4 when dbl(4) is called. 
# It does not make a difference in this example, but it does in the example below.

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(8))