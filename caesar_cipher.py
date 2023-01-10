import os
from caesar_cipher_arts import logo

alphabet_letters = [
    'A','B','C','D','E',
    'F','G','H','I','J',
    'K','L','M','N','O',
    'P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

clear_console = lambda: os.system("clear")

def encrypt(plain_text, shift_amount):
    shift_amount = shift_amount % 26
    encoded_text = ''
    alphabet_shifted = alphabet_letters[shift_amount:] + alphabet_letters[:shift_amount]
    for each_letter in plain_text:
        if each_letter in alphabet_letters:
            encoded_text += alphabet_shifted[alphabet_letters.index(each_letter)]

    return encoded_text


def decrypt(cipher_text, shift_amount):
    shift_amount = shift_amount % 26
    decoded_text = ''
    alphabet_shifted = alphabet_letters[shift_amount:] + alphabet_letters[:shift_amount]
    for each_letter in cipher_text:
        if each_letter in alphabet_shifted:
            decoded_text += alphabet_letters[alphabet_shifted.index(each_letter)]

    return decoded_text   


option = 0
clear_console()
while not option == 3:
    if option == 0:
        print(logo())
    option = int(input("\n [1] Encrypt \n [2] Decrypt \n [3] Exit \n \n Select an option: "))
    if option == 1:
        clear_console()
        message = str(input('Type your message: ')).upper()
        shift_amount = int(input('Type the shift number? ')) 
        encrypted_text = encrypt(plain_text=message, shift_amount=shift_amount)
        print(f"your encrypted message is {encrypted_text}")

    if option == 2:
        clear_console()
        message = str(input('Type your message: ')).upper()
        shift_amount = int(input('Type the shift number? ')) 
        decrypted_text = decrypt(cipher_text=message, shift_amount=shift_amount)
        print(f"Your decrypted message is {decrypted_text}")
