Minimum_voting_age = 18
def check_voter_eligibility():
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))

    if age >= Minimum_voting_age:
        print(f"Hello {name},You are eligible to vote")
    else:
        print(f"Sorry {name},You are Not eligible to Vote. You Must be at least {Minimum_voting_age}years old.")
check_voter_eligibility()