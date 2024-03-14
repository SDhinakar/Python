height=int(input("Enter the height in cm : "))
bill=0
if(height>=3):
    print("You can ride")
    age=int(input("Enter your age : "))
    if age<12:
        bill=150
        print("Please pay 150 Rs.")
    elif age<=18:
        bill=250
        print("Please pay 250 Rs.")
    else:
        bill=500
        print("Please pay 500 Rs.")

    want_photo=input("Do you want a photo? (Y/N) : ")
    if want_photo=="Y" or want_photo=="y":
        bill=bill+50

    print(f"Your total bill is {bill} Rs.")
    print("Enjoy your ride")

else:
    print("You cannot ride")

print("Bye !!!")