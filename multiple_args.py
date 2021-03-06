# def foo(first, second, third, *therest):
#     print("First: %s" %(first))
#     print("Second: %s" %(second))
#     print("Third: %s" %(third))
#     print("And all the rest... %s" %(list(therest)))

# foo(1,2,3,4,5)

def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

#Ex 3
def bar_1(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar_1(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))