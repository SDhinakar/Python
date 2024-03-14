height=int(input("Enter the height of the person in cm : "))
if height>140:
    print("Height is normal")
    age=int(input("Enter the age of the person : "))
    if(age>=18):
        print("Can ride the roller coaster ")
    elif(age>20):
        print("Can ride the roller coaster and can ride the car.")
    elif(age>25):
        print("Can ride the roller coaster and can ride the car and can drive the car.")
    else:
        print("Can't ride the roller coaster")
else:
    print("Height is not normal.")