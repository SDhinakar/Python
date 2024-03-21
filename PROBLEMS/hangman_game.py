import random
import string

def hangman():
    words_list = ['apple', 'fig', 'grape']
    word = random.choice(words_list)
    guessed_letters = []
    tries = 6

    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'

        print(f'Word: {guessed_word}')
        print(f'Guessed Letters: {", ".join(guessed_letters)}')
        print(f'Tries left: {tries}')

        if guessed_word == word:
            print('Congratulations! You guessed the word.')
            return

        guess = input('Enter a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        elif guess not in string.ascii_lowercase:
            print('Please enter a valid lowercase letter.')
        elif len(guess) != 1:
            print('Please enter only one letter at a time.')
        elif guess in word:
            guessed_letters.append(guess)
        else:
            tries -= 1
            guessed_letters.append(guess)
            print('Wrong guess.')

    print(f'Game over. The word was {word}.')

hangman()
