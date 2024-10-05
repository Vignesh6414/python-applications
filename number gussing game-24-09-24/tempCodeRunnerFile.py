import random
def guess_number(l,h):
    low = l
    high  =h
    values =int(input("Enter the Condition: "))
    value = values
    while True:
        computer = random.randint(low,high)
        print(computer)
       

        if computer < value:

            print("Your Value is low")
            low = computer + 1
                
        elif computer > value:

            print("your Value is High")
            high = computer - 1

        elif computer == value:
            print(f"Congrats:{computer} 🎊🎊🎊 You win")
            return
        else:
            print("invalid")
guess_number(1,100)    