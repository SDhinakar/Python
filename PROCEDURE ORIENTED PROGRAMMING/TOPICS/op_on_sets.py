set1={'Ram','Shyam','Jenny','Jiya','Aakash'}
set2={'Jiya','Aakash'}

print(set1.isdisjoint(set2))  # returns true if no common data is present
# print(set1.isdisjoint(['Ram','Shyam','Jenny']))  # returns false if common data is present

print(set2.issubset(set1))  # subset = set2 is present in set1
# print(set1 <= set1)

print(set1.issuperset(set2)) # superset = set1 is present in set2
# print(set1>=set2)

# set2.clear()  # clears the values of set2
# print(set2)

# del set2    # deletes the set2
# print(set2) # NameError: name 'set2' is not defined