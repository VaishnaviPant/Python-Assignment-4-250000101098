x = 10

def modify():
    global x
    x = 50
    print("Inside function:", x)

modify()

print("Outside function:", x)