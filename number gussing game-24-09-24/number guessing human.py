import random
def number_guessing_game():
    computer = random.randint(1,10)
    chance = 1
    max_chance = 10
    print(f"guess hte number 1 to 10")
    while chance < max_chance:
        guess = int(input("Enter the guess number: "))
        chance += 1

        if guess >= 11:
            print("invalid Number")
        elif guess < computer:
            print("Too Low! Try Again")
        elif guess > computer:
            print("Too High! Try Again")
        else:
            print("Congratulations🎊you win" ) 
            break
    if chance == max_chance:
        print(f"Sorry you used all attempts  number was {computer}")
number_guessing_game()

