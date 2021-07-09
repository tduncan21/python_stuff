import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_win_scenarios = [(rock, "2"), (paper, "0"), (scissors, "1")]


#Get user input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

#Select Random int for computer 0 - 2
computer_choice = random.randint(0, 2)

#Handle win or lose
if computer_choice == int(user_win_scenarios[user_input][1]):
    #user won
    print(f"User:\n{user_win_scenarios[user_input][0]}\n Computer:\n{user_win_scenarios[computer_choice][0]}\n You won!")
elif computer_choice == user_input:
    print(f"User:\n{user_win_scenarios[user_input][0]}\n Computer:\n{user_win_scenarios[computer_choice][0]}\n Draw!")
else:
    #user lost
    print(f"User:\n{user_win_scenarios[user_input][0]}\n Computer:\n{user_win_scenarios[computer_choice][0]}\n You lost!")
