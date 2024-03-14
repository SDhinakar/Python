pizza = input("Enter the type of pizza you want (S/M/L) : ")
bill = 0

if( pizza=='s' or pizza=='S'):
    bill=100
    print("Small pizza costs 100 Rs.")
elif(pizza=='m' or pizza=='M'):
    bill=200
    print("Medium pizza costs 200 Rs.")
elif(pizza=='l' or pizza=='L'):
    bill=300
    print("Large pizza costs 300 Rs.")
else:
    print("Invalid choice")
    exit()


pepparoni=input("Do you want pepparoni? (Y/N) : ")
if(pepparoni=='Y' or pepparoni=='y'):
    if(pizza=='s' or pizza=='S'):
        bill=bill+20
    else:
        bill+=50

cheese=input("Do you want extra cheese? (Y/N) : ")
if(cheese=='Y' or cheese=='y'):
    bill+=10

print(f"Your total bill is {bill} Rs.")