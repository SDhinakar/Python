year=int(input("Enter the year : "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

if(year%4==0 and year%100!=0 or year%400==0):  #  if( (year%4==0 and year%100!=0) or (year%400==0) ):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# def leap_year(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         return f"{year} is a leap year"
#     else:
#         return f"{year} is not a leap year"
    
# print(leap_year(year))