# # default    positional   keyword    variable positional    variable keyword

# # We need to give non-default arguments first and then default arguments to avoid error.

# def greet(name,dept):
#     print(f"hello , {name}")
#     print(f"Are you from {dept} department ?") # here name and dept are positional arguments
# greet(name="John",dept="CSE") # keyword arguments

# def greet(name,dept):
#     print(f"hello , {name}")
#     print(f"Are you from {dept} department ?") # here name and dept are positional arguments
# greet('john','CSE')  # Positional arguments

# def greet(name,dept="CSE"): # Default arguments
#     print(f"hello , {name}") # here dept is a default argument
#     print(f"Are you from {dept} department ?") 
# greet('john') 

'''***************************'''

def add(name,*numbers): # Variable Positional arguments
    c=0
    print(name)
    for i in numbers:
        c+=i
    print(f"The sum is :{c}")
add('dhina',5,5,5,5,5,5,5,5,5,5) # Variable Positional arguments

def info_person(*args,**kwargs): # Variable Keyword arguments
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print(args)

info_person(12,34,name="ram",age=25,dept="CSE",city="Chennai")
info_person(name="piggy",age=25,dept="CSE")
info_person(name="dhana",age=25)
info_person(name="dharun")

