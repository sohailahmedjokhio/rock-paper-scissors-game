# Rock-Paper-Scissors Game

This is a simple Python implementation of the classic Rock-Paper-Scissors game. In this game, the player chooses between Rock, Paper, or Scissors, and competes against the computer's randomly selected choice. The winner is determined based on the rules: Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock.

# How to Play
1. Clone the repository to your local machine.
   <pre>git clone https://github.com/your-username/rock-paper-scissors.git</pre>
2. Navigate to the project directory.
   <pre>cd rock-paper-scissors</pre>
3. Run the Python script.
   <pre>python rock_paper_scissors.py</pre>
4. Follow the on-screen instructions to input your choice (0 for Rock, 1 for Paper, or 2 for Scissors).


# Game Rules
- Rock crushes Scissors.
- Scissors cuts Paper.
- Paper covers Rock.

# ASCII Art Representation
The game includes ASCII art representations for Rock, Paper, and Scissors to make the gameplay more visually appealing.

<pre>
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
</pre>

# Game Logic
The game logic is implemented to determine the winner based on the choices made by the player and the computer. The comparison follows the traditional rules of Rock-Paper-Scissors.

<pre>
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
</pre>

# Error Handling
The script includes error handling to ensure that the user's input is within the valid range (0 to 2). If the user provides an invalid input, the script will display an error message.

<pre>
if 0 <= your_choice < len(choices):
    # Game logic goes here
else:
    print("Invalid input. Please select from 0 to 2.")
</pre>

# Contribution
Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and suggestions are highly appreciated.

# License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt). Feel free to use and modify the code as per the terms of the license.