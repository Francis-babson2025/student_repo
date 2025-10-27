
def scope_int(x):
    x += 1
    print('inside:', x)

x = 5
scope_int(x)
print('outside:' , x)

def scope_list(myList):
    myList[0] += 1
    print('inside:', myList)

myList =[1, 2, 3]
scope_list(myList)
print('outside:' , myList)