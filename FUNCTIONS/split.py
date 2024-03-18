a=input("Enter any string : ")
output=a.split(" ")  # split() method is used to split the string into a list of strings and inside the split() method, 
print(output)        # we can pass the separator as an argument.

second_output=a.split("a")
print(second_output)

output=a.split(" ",2)  # split() method can also take a second argument which is the maximum number of splits to be done.
print(output)          # In this case, the string will be split into 3 parts.