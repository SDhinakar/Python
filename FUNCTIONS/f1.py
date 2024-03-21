# def add(a,b):
#     c=a+b
#     print(f"The sum is :{c}")

# add(10,20)
# add(30) # TypeError: add() missing 1 required positional argument: 'b'

# def greet(name):
#     print(f"hello , {name}")
#     print("How are you?")
# greet(input("Enter your name : "))

def product(*numbers):
    print(f"Numbers are : {numbers}")
    product=1
    for i in numbers:
        product*=i
    print(f"The product is : {product}")
product(12,52,63,68,47)