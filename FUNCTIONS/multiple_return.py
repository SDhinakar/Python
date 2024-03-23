# import statistics
# import math
# def mean_median_mode(list1):
#     return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

# a,b,c=mean_median_mode([3,5,45,3,2,1,89])
# print(f"Mean is : {a}\nMedian is : {b}\nMode is : {c}")


# def add(a,b):
#     if a==0 and b==0:
#         return "Both are zero"
#     else:
#         return a+b
    
# print(add(int(input("Enter the first number : ")),int(input("Enter the second number : "))))

def add(a, b):
    if not a and not b:
        return "Both are empty"
    else:
        return a + b
    
print(add(input("Enter the first number : "), input("Enter the second number : ")))
