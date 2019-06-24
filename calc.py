print("Enter two integers for calculation.")
x = int(input("First number: "))
y = int(input("Second number: "))

def add(x,y):
    return x + y
def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def mult(x,y):
    return x * y



print(x," + ",y, "is equal to: ", add(x,y))
print(x," - ",y, "is equal to: ", sub(x,y))
print(x," / ",y, "is equal to: ", div(x,y))
print(x," * ",y, "is equal to: ", mult(x,y))

