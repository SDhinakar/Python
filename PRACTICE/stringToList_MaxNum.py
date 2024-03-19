#To find maximum number from a list of numbers

numbers=input("Enter list of numbers : ")
numbers_list=numbers.split()

# for i in numbers_list:
#     numbers_list[i]=int(numbers_list[i]) #TypeError: list indices must be integers or slices, not str
# print(numbers_list)

for i in range(0,len(numbers_list)):  # range(0,len(numbers_list)) ==   range(len(numbers_list))
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)

max_num=numbers_list[0]

for i in numbers_list:
    if i>max_num:
        max_num=i       # print(max(numbers_list)) gives same result

print(f"The maximum number is : {max_num}.")