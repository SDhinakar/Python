set1={0,10,1.5,'dhina',True,10,1}
print(set1)

set1.add(99)
print(set1)

set1.add((1.1,15,89))
print(set1)

# set1.remove(1.5)
# print(set1) # gives error if element is not present
# set1.discard(10)
# print(set1) # no error though element is not present
# set1.clear()
# print(set1) # empty set returns set()

# set1.pop()
# print(set1.pop())
# print(set1)

# print(type(set1))
# print(len(set1))

# set2=set()
# print(type(set2))  #set because of empty set
# set2={}
# print(type(set2))   #dict because of empty curly braces

# print(set1[3]) #TypeError: 'set' object is not subscriptable
# print(set1[3:5]) #TypeError: 'set' object is not subscriptable
# set2[3]=5 #TypeError: 'set' object does not support item assignment