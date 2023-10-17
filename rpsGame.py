import random

user_wins = 0
computer_wins = 0

while True:
    options = ["rock", "paper", "scissor"]
    user_input = input("Enter Rock/Paper/Scissor or Q to quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock : 0 , paper : 1, scissor : 2
    computer_pick = options[random_number]
    print("Computer pick :", computer_pick)

    if user_input == "rock" and computer_pick == "scissor":
        print("You won :)")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won :)")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won :)")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie :)")
    else:
        print("You've lost :(")
        computer_wins += 1
    print()
    print("Your score :", user_wins)
    print("Computer score :", computer_wins)
    print()
