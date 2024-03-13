# identity operator is used to compare the memory location of two objects
# "is" and "is not" are the identity operators in python

a=5
b=5.0
c=5
d='5'

print(a==b) #compares the value
print(a is b) #compares the memory location
print(a is c)
print(a is d)
print(a is not b)

print(id(a))
print(id(b))
print(id(c))

print(id(a)==id(b))
print(id(a)==id(c))
print(id(a)==id(d))

# e=5
# print(id(e))
# print(e)
# e=6
# print(id(e))
# print(e)
# print(e is e)  # True since both e and e are pointing to the same memory location