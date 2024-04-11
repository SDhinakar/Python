import math

def paint_calculation(height,width,cover):
    area=height*width
    number_of_cans=math.ceil(area/cover) # ceil function is used to round up the number
    number_of_cans=area/cover
    print(f"You will need {number_of_cans} cans of paint")

h=int(input("Enter the height of the wall : "))
w=int(input("Enter the width of the wall : "))
coverage=5

paint_calculation(height=h,width=w,cover=coverage) # Keyword arguments