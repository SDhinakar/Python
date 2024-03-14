weight=float(input("Enter the Weight in Kilograms: "))
height=float(input("Enter the Height in metres: "))

BMI=weight/(height**2)

if(BMI<18.5):
    print(f"The BMI is {BMI} and the person is Underweight")
elif(BMI>=18.5 and BMI<25):
    print(f"The BMI is {BMI} and the person is Normal")
elif(BMI>=25 and BMI<30):
    print(f"The BMI is {BMI} and the person is Overweight")
elif(BMI>=30 and BMI <35):
    print(f"The BMI is {BMI} and the person is obese.")
else:
    print(f"The BMI is {BMI} and the person is clinically obese.")