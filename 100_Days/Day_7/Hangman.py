import random
import hangman_words
import hangman_art


def get_user_guess():
    user_guess = input("Guess a letter: ")
    return user_guess


def user_guess_exists(user_guess):
    if user_guess in word_to_guess:
        return True
    return False


def guess_correct(user_guess):
    for x in range(len(reveal_word)):
        if user_guess == word_to_guess[x]:
            reveal_word[x] = user_guess
            word_to_guess[x] = " "
    return

def guess_incorrect():
    global user_lives
    print(hangman_art.stages[user_lives])
    user_lives -= 1
    print(f"Letter does not exist {user_lives + 1} guesses remaining")
    return


def handle_win_loss():
    global is_playing
    if win_condition == word_to_guess:
        print("You won!")
        is_playing = False
    elif user_lives < 0:
        print(f"You lost. The word was {winning_word}")
        is_playing = False
    return


def join_string(word_to_join):
    display_word = ""
    for letter in word_to_join:
        display_word += letter
    return display_word

def initialize_game():
    global list_of_words, word_to_guess, winning_word, win_condition, reveal_word, is_playing, user_lives

    list_of_words = hangman_words.get_words()
    word_to_guess = list(random.choice(list_of_words))
    winning_word = join_string(word_to_guess)
    win_condition = [" " for x in word_to_guess]
    reveal_word = ["_" for x in word_to_guess]

    is_playing = True
    user_lives = len(hangman_art.stages) - 1

    print(hangman_art.logo)
    print(join_string(reveal_word))


def start_game():
    while is_playing:    
        # get user guess
        user_guess = get_user_guess()
        # check if guess is correct
        if user_guess_exists(user_guess):
            #if it is update letters
            guess_correct(user_guess)
        else:
            #if not, subtract lives 
            guess_incorrect()
        # Print word
        print(join_string(reveal_word))
        # check if win loss
            #if win, print win and exit
            #if loss, print loss and exit
        handle_win_loss()
        # repeat


initialize_game()
start_game()
