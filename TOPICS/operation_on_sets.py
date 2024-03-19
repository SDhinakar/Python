
set1={'Ram','Shyam','Ghanshyam','Radha','dhina','Sita'}
set2={'Radha','Sita','Ghanshyam','dhina','Krishna'}
# print(set1.union(set2))
# print(set1 | set2)

set3={'dhina','ajey'}
# print(set1.union(set2,set3))
# print(set1 | set2 |set3 )

# print(set3.union(('ram','vicky')))

# set1.update(['jenny','Jenny','jenny']) # case sensitive and duplicates are not allowed in set
# print(set1)

# set1|=set3    # used for updating set1 with set3 
# print(set1) 

# print(set1.intersection(set2,set3)) # used to get the common datas

# print(set1 & set3)  # prints the common datae

set1.intersection_update(['black','dhins'])
print(set1) 


set1={'Ram','Shyam','Jenny'}
set2={'Jenny','Jiya','Aakash'}
set3={'Ankur','Pradeep','Ram'}
# print(set1.difference(set2))
# print(set1 - set2)
# print(set1.difference(set2,set3))
# set1.difference_update(set2)
# print(set1)
# print(set1.symmetric_difference(set2))
print(set1^set2^set3)