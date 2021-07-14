from caesar_cipher_alphabet import get_alphabet


def encrypt(user_message, shift):
    encrypted_message = ""
    for letter in user_message:
        shifted_letter_index = 0
        index = alphabet.index(letter)
        index += shift
        if index > len(alphabet)-1:
            shifted_letter_index = index - len(alphabet) + 1
        else:
            shifted_letter_index = index
        encrypted_message += alphabet[shifted_letter_index]
    return encrypted_message


def decrypt(user_message, shift):
    encrypted_message = ""
    for letter in user_message:
        shifted_letter_index = 0
        index = alphabet.index(letter)
        index -= shift
        if index < 0:
            shifted_letter_index = len(alphabet) + index - 1
        else:
            shifted_letter_index = index
        encrypted_message += alphabet[shifted_letter_index]
    return encrypted_message


def continue_cipher():
    global ciphering
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if user_input == "no":
        ciphering = False
        return
    return


ciphering = True
alphabet = get_alphabet()

while ciphering:
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" )
    user_message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if user_input == "encode":
        print(encrypt(user_message, shift))
    else:
        print(decrypt(user_message, shift))
    continue_cipher()