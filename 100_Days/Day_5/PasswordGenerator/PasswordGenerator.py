#Password Generator Project
import random


def generate_random_letters(num_chars):
    letters_pool = ""
    while num_chars > 0:
        index = generate_random_number(len(letters) - 1)
        letters_pool += letters[index]
        num_chars -= 1
    return letters_pool


def generate_random_numbers(num_chars):
    numbers_pool = ""
    while num_chars > 0:
        index = generate_random_number(len(numbers) - 1)
        numbers_pool += numbers[index]
        num_chars -= 1
    return numbers_pool


def generate_random_symbols(num_chars):
    symbols_pool = ""
    while num_chars > 0:
        index = generate_random_number(len(symbols) - 1)
        symbols_pool += symbols[index]
        num_chars -= 1
    return symbols_pool


def generate_pool(num_letters, num_numbers, num_symbols):
    char_pool = ""
    #get pool to choose characters from
    char_pool += generate_random_letters(num_letters)
    char_pool += generate_random_numbers(num_numbers)
    char_pool += generate_random_symbols(num_symbols)
    #convert string to list
    char_pool = list(char_pool)
    #pass to generate_password_rand
    generate_password_rand(char_pool)
    return


def generate_password_rand(char_pool):
    chars_left = len(char_pool)
    final_pass = ""
    while chars_left > 1:
        #select random int in range of character pool
        index = generate_random_number(chars_left - 1)
        #append to final password
        chosen_char = char_pool[index]
        final_pass += chosen_char
        #remove character from pool
        char_pool.remove(chosen_char)
        #repeat until pool has len 1
        chars_left -= 1
    #append last character to final password
    final_pass += char_pool[0]
    #output final password
    print(final_pass)
    return 


def generate_random_number(num):
    #generate random number in given range
    #return number
    return random.randint(0, num)
    


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generate_pool(nr_letters, nr_symbols, nr_numbers)
