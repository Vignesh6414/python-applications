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

# def number_guessing(l,h):
#     low=l
#     high = h
#     print(low, high)
#     while True:
#         computer_guess = (low + high )//2
#         value = input(f"{computer_guess} Enter the vale (L)- Low, (H) - High, (C) - Correct: ").upper()

#         if "L" in value:
#             low = computer_guess
#             number_guessing(low,high)
#             print("Your Value is low")

#         elif"H" in value:
#             high = computer_guess
#             number_guessing(low,high)
#             print("your Value is High")

#         elif"C" in value:
#             print("Congrats🎊 correct answer")
#             break
#         else:
#             None
            
# number_guessing(1,100)