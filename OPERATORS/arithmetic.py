"""
P E M D A S = ARITHMETIC OPERATORS
()
**          R-L
* / // %    L-R
+ -         L-R
"""

#To calculate BMI
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI=weight/(height**2)
print(BMI)