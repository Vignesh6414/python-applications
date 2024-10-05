 
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Meenatchi2310",
  database="bank"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE customers (Name VARCHAR(255),email VARCHAR(255),password INT, Address VARCHAR(255))")

mycursor.execute("INSERT INTO customers VALUES ('', '')")
mycursor.execute("")
mycursor.execute("Select * from customers")
myresult = mycursors.fetchall()


print(myresult)
mydb.commit()


user = {}
money = 0.0
print()

print(""" Hello Solider 
              WELCOME To BANK """)
def User():
    while True:
        print(""" please Select the Option
                    (1) Open Account
                    (2) Sign in
                    (3) Withdraw
                    (4) Check Balance
                    (5) Exit
                            """)
        User = int(input("Enter the Option: "))
        if 1 == User:
            sign_up()
        elif 2 == User:
            sign_in()
        elif 3 == User:
            sign_in()
            debit_money()
        elif 4 == User:
            sign_in()
            balance()
        elif 6 <= User:
            print("invalid input pls try again")
        else:  
            5 == User
            print("Thank you visit again solider")
            break  
        break      


def sign_up():
    
    name = input("Enter the Full name: ")
    email = input("Enter your email ID: ")
    passkey = int(input("Enter the password only numbers: "))
    address = input("Enter the Address: ")
    print("Your Success fully signed")
    global user
    user = {"Name":name,"email":email,"password":passkey,"Address":address}

def sign_in():
    Name = input("Enter the Full name: ")
    Passkey = int(input("Enter the password only numbers: "))

    if user.get("Name") == Name and user.get("password") == Passkey:
        print("Your successfully Sign in")
        while  True:
            print(""" please Select the Option
                
                (1) ADD Amount
                (2) Debit Amount
                (3) Check Balance
                (4) More
                (5) Exit
                        """)
            choice = int(input("Enter the Choice: "))
            if 1 == choice:
                add_money()
            elif 2 == choice:
                debit_money()
            elif 3 == choice:
                balance()
            elif 4 == choice:
                More()
            elif 5 == choice:
                print(f"Thank you visit {Name} again")
                break
            else:
                print("pls try again")
    else:
        print("please Try again")
        
def add_money():
    global money
    print("Deposit you Money")
    Amount = float(input("Enter the Amount: "))
    money += Amount
    print(f"Deposit Amount {money} success fully Deposited")

def debit_money():
    global money
    print("Debit Your Amount")
    amount = float(input("Enter the Debit Amount: "))
    money -= amount
    print(f"Debit Amount {amount} success fully Debit")
    print("Thank you visit again")

def balance():
    print(f"Your Available balance is {money}")

def More():
    while  True:
        print(""" please Select the Option
            
            (1) Change Name
            (2) change password
            (3) change E-mail ID 
            (4) sign in
            (5) Exit
                    """)
        change = int(input("Enter the option: "))
        if 1 == change:
            sign_up()
        elif 2 == change:
            sign_up()
        elif 3 == change:
            sign_up()
        elif 4 == change:
            sign_in()
        elif 5 == change:
            print("Thank you visit again")
            break
        break
User()
sign_up()           
sign_in() 
