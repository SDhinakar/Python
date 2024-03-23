a=10
def display():
    global a # global keyword is used to access the global variable inside the function and to modify the global variable
    a=a+10
    print(a)
display()