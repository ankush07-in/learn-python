# global keyword changes the global variable

a = 89 # global variable

def fun():
    global a
    a = 3 # local variable of this function
    print(a)

fun()
print(a)