a=input("Enter a: ")
b=input("Enter b: ") #in input() method, the value is always a string
temp=a
a=b
b=temp
print("a:",a)
print("b: "+b) #since the value of b is string, we can use + to concatenate