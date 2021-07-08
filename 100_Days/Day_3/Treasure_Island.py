print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload




def handle_game_over(user_input):
    if user_input not in lose_prompts:
        print("Your choice destroyed the world! Game over")
        return
    print(lose_prompts[user_input])


def handle_win():
    print("Congratulations, you found the treasure!")
    return


def handle_user_choice(user_input, continue_choice):
    if user_input != continue_choice:
        handle_game_over(user_input)
        return False
    return True


def get_user_input(prompt):
    user_input = input(prompt)
    return user_input


def start_game(prompts_choice):
    isPlaying = True
    prompt_choice = prompts_choice[0]
    index = 0
    while isPlaying:
        user_input = get_user_input(prompt_choice[0])
        if handle_user_choice(user_input, prompt_choice[1]):
            index += 1
            if index >= len(prompts_choice):
                handle_win()
                return
            prompt_choice = prompts_choice[index]
        else:
            isPlaying = False
    return


prompts_choice = [("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n", "left"),
        ("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n", "wait"),
        ("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n", "yellow"),
        ("You arrive at a bottomless pit. Do you 'jump' or 'leave'? \n", "jump")]

lose_prompts = {"right" : "You fell into a hole. Game Over.",
        "swim" : "You get attacked by an angry trout. Game Over.",
        "blue" : "You enter a room of beasts. Game Over.",
        "red" : "It's a room full of fire. Game Over.",
        "leave" : "You turn around to a room full of beasts. Game Over"}

start_game(prompts_choice)