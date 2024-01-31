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

import random

choices = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if 0 <= your_choice < len(choices):
    computer_random = random.randint(0, len(choices) - 1)

    print("\nComputer Choice:")
    print(choices[computer_random])

    print("Your Choice:")
    print(choices[your_choice])

    if choices[computer_random] == scissors and choices[your_choice] == rock:
        print("You Win!")
    elif choices[computer_random] == rock and choices[your_choice] == scissors:
        print("You Win!")
    elif choices[computer_random] == paper and choices[your_choice] == rock:
        print("You Win!")
    elif choices[computer_random] == choices[your_choice]:
        print("\nIt's a Draw!")
    else:
        print("You Lose!")
else:
    print("Invalid input. Please select from 0 to 2.")