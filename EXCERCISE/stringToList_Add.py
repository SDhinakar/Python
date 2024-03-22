height=input('Enter all the heights : ')
height_list=height.split() #split() method is used to split the string into a list of strings

count=0
for i in height_list:    # count=len(height_list) will also give the same result
    count+=1

for i in range(count):
    height_list[i]=int(height_list[i]) # typecasting list of strings into integers using int() function
print(height_list)

total=0
for i in height_list:
    total+=i
print(f"The total height is : {total}.")

avg=total/count
print(f"The average height is : {round(avg)}.")