import random

list_of_words = [
"rehearsal",
"prosper",
"proposal",
"hear",
"trust",
"profit",
"include",
"threaten",
"crash",
"attraction",
"car",
"opposed",
"winter",
"bulb",
"lamb",
"common",
"amuse",
"plant",
"illness",
"example",
"rehabilitation",
"revise",
"power",
"sum",
"polish",
"productive",
"drill",
"TRUE",
"guitar",
"defendant",
"review",
"division",
"cart",
"creation",
"guess",
"jest",
"grave",
"shape",
"fiction",
"embryo",
"remember",
"wire",
"show",
"gallery",
"calm",
"acid",
"decline",
"salad",
"grief",
"regulation"
]

def generate_random_int(max_num):
    return random.randint(0, max_num-1)


index = generate_random_int(len(list_of_words))
word_to_guess = list(list_of_words[index])
print(word_to_guess)
reveal_word = ["_" for x in word_to_guess]

display_word = ""
for letter in reveal_word:
    display_word += letter
print(display_word)

has_won = False
has_lost = False
user_lives = 5


while not has_won or has_lost:
    
    user_guess = input("Guess a letter: ")
    user_guess_exists = False
    for x in range(len(word_to_guess)):
        if user_guess == word_to_guess[x]:
            reveal_word[x] = user_guess
            user_guess_exists = True

    if not user_guess_exists:
        print("Letter not found in word")
        user_lives -= 1
    if user_lives == 0:
        has_lost = True
        print("You lost")
        break
        
        
    display_word = ""
    for letter in reveal_word:
        display_word += letter

    if list(display_word) == word_to_guess:
        has_won = True

    print(display_word)


# Hangman game cycle
    # Get word to guess
    # Ask user for guess 
    # If guess was a letter, check if it is in the guessed word.
        # If it is, reveal letter
    # Check if user has won
        # If no more letters in word, user won
        # If not ask for guess
    # If guess was incorrect, subtract from lives