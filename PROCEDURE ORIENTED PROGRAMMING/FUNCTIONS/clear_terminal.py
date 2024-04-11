import os
def clear_terminal():
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    c=a+b
    print(f"The sum is :{c}")
    choice=input("Press 'c' to clear the terminal and continue or 'x' to exit : ").lower()
    if choice=='c':
        os.system('cls') # windows
        
        clear_terminal()
    else :
        exit()
    
clear_terminal()