#to calculate sum of even numbers from 1 to 100 includeing 1 & 100

a=range(1,101)
total=0
for i in a:         # for i in range(1,101):
    if(i%2==0):
        total+=i
print(f"The total is {total}")


# a=range(-1,-21,-1)    # range(start,stop,step)  # range(1,20,10) == range(1,20,10) == range(1,20,10,1)
# total=0
# for i in a:
#     total+=i
# print(total)

# for i in range(1,20):
#     print(i)