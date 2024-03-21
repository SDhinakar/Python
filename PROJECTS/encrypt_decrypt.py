alphabet = 'abcdefghijklmnopqrstuvwxyz'
positions = {char: index for index, char in enumerate(alphabet)}

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in positions:
            position = positions[char]
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ''
    for char in cipher_text:
        if char in positions:
            position = positions[char]
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here's the text after decryption: {plain_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("What do you want to do? (encrypt/decrypt):\n").lower()
    text = input("Type your Message:\n").lower()
    shift = int(input("Enter shift key:\n"))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    else:
        decryption(text, shift)
    play_again = input("Do you want to end the program? (yes/no):\n")
    if play_again == "yes":
        wanna_end = True
    else:
        wanna_end = False
