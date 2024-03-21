import math
def prime_checker(number):
    is_prime=1
    if number<2:
        is_prime=0
    for i in range(2,math.ceil(number/2)+1): #
        if number%i==0:
            is_prime=False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

n=int(input("Enter a number : "))
prime_checker(n)