import random
user_choice=int(input("Enter your choice : Type 0 for Rock, 1 for Paper and 2 for Scissor : "))
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, you lose!")
else:
    list=["Rock","Paper","Scissor"]
    print(f"User chose : {list[user_choice]}")

    computer_choice=random.randint(0,2)
    print(f"Bot  chose : {list[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")