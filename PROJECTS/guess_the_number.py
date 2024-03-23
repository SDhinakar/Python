import random
import guess_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"You got it! The answer was {answer}")


def game():
    print(guess_art.logo)
    print("Let me think of a number between 1 - 50.")
    answer=random.randint(1,50)
    level=input("Choose a level: easy,hard: ").lower()
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("Invalid level chosen.")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number=int(input("Make a guess: "))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("You've run out of guesses, you lose.")
            break
        elif guessed_number!=answer:
            print("Guess again.")
        else:
            print("You win!")
game()