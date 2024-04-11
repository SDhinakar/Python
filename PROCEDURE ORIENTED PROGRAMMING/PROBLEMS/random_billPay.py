import random

a=input("Enter the names : ")
names=a.split(",")
print(names)

# choice=random.choice(names)
# print(f"{choice} will pay the bill today.")

length=len(names)
choice=random.randint(0,length-1)
print(f"{names[choice]} will pay the bill today.")