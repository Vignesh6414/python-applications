import random

def rack_paper_scissors():
    rock = 1
    paper = 2
    scissors = 3
    player_choice = int(input("Enter the any one number 1 2 3 :"))
    computer = random.randint(1,3)
    print(f"you chose: {player_choice}")
    print(f"computer chose:{computer}")
    if player_choice == computer:
        print("Draw")
    elif (player_choice == 1 and computer == 3) or \
       (player_choice == 2 and computer == 1) or \
       (player_choice == 3 and computer == 2):
        print("You win!")
    else:
        print("Computer Wins")
rack_paper_scissors()