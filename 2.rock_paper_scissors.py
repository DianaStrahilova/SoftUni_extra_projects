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

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input! Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

if player_move == rock and computer_move == scissors or \
    player_move == paper and computer_move == rock or \
    player_move == scissors and computer_move == paper:
    print(f"You Win! {player_move}")
    print(f"Computer move was: {computer_move}")
elif player_move == computer_move:
    print(f"It's a draw! {player_move}")
else:
    print(f"You lose! {player_move}")
    print(f"Computer move was: {computer_move}")


