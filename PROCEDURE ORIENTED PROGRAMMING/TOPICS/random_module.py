import random

a=random.randint(0,1)     # randint returns an element value either  a or b
print(a)

a=random.randrange(1,10)  # randrange return an element between    a <= x < b
a=random.random()         # random returns a float value between 0.0 <= x < 1.0
a=random.uniform(1,3)     # uniform return a float value between  a  <= x < b
print(a)

# l=[-1,0,2 ,6 ,8, 9, 10]
# a=random.choice(l)         # choice return a random element from the list
# print(a)

# l=[-1,0,2 ,6 ,8, 9, 10]
# random.shuffle(l)          # shuffle return the shuffled entire array or list
# print(l)