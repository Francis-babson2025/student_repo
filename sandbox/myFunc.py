x = 5
num = 5
print(id(x))
def myFunc():
    print(id(num))
    z += 1
    print(id(z))
    return z

y = myFunc(x)
print(id(y))