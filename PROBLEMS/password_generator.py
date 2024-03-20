import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+','-','?','<','>','/']

print("Welcome to the PyPassword Generator!")
num_letters=int(input("How many letters would you like in your password?\n"))
num_symbols=int(input(f"How many symbols would you like?\n"))
num_numbers=int(input(f"How many numbers would you like?\n"))

password_list=[] # empty list
for i in range(1,num_letters+1):
    password_list+=random.choice(letters)

for i in range(1,num_symbols+1):
    password_list+=random.choice(symbols) # concatenating the list with the random choice of symbols

for i in range(1,num_numbers+1):
    password_list+=random.choice(numbers)

random.shuffle(password_list) # shuffles the list
print(password_list)    

password="" # empty string
for i in password_list:
    password+=i     # concatenating the elements of the list to the string
print(f"Your password is {password}")