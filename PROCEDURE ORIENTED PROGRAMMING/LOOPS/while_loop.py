# while loop is used when the user does not know the number of iterations in advance.
# sentinels are used to stop the loop.

# count=1
# while count>0:      #while count>0: print(count); count-=1  #single line of code
#     print(count)
#     count=1
#     if count==3:
#         break
# else:
#     print("Done without interruption")
# print("Done")


# number=int(input("Enter a number(-1 to quit): "))
# while(number!=-1):
#     print(number)
#     number=int(input("Enter a number(k-1 to quit): "))
# else:
#     print("Done without interruption")
# print("Done")

# count=0
# while True:
#     print(count)
#     count+=1
#     if(count==5):
#         break
# else:
#     print("Done without interruption")
# print("Done")

total=0
num=int(input("Enter a number(0 to quit): "))
while num!=0:
    total+=num
    num=int(input("Enter a number(0 to quit): "))
print("Total: ",total)