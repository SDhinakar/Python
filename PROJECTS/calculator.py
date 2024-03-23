import os 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

def calculator():
    number1=int(input("Enter first number : "))
    for op in operations:
        print(op)
    continue_flag=True

    while continue_flag:
        symbol=input("Enter the operation : ")
        number2=int(input("Enter second number : "))
        calc_function=operations[symbol]
        result=calc_function(number1,number2)
        print(f"{number1} {symbol} {number2} = {result}")

        should_continue=input(f"Enter 'y' to continue calculation with {result} or 'n' to start a new calculation or 'x' to exit : ").lower()
        if should_continue=='y':
            number1=result
        elif should_continue=='n':
            continue_flag=False
            os.system('cls') # clears the terminal for new calculation
            calculator()
        else:
            continue_flag=False
            print("Goodbye")
calculator()
