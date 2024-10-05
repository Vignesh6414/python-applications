import mysql.connector
import random

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Meenatchi2310",
            database="myBank"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

import random

def generate_account_number():
    return random.randint(100000, 999999)  # Generate a 6-digit number

def sign_up(mydb, mycursor):
    print("Please fill your Details.")
    name = input("Enter the Full name: ")
    email = input("Enter your email ID: ")
    passkey = input("Enter the password (numbers only, up to 6 digits): ")
    address = input("Enter the Address: ")
    
    # Validate password
    if not passkey.isdigit() or len(passkey) > 6:
        print("Invalid password. Please use up to 6 digits only.")
        return

    account_number = generate_account_number()
    try:
        mydb.start_transaction()
        
        mycursor.execute("INSERT INTO customers (Name, Email, PASSWORD, ADDRESS) VALUES (%s, %s, %s, %s)", 
                         (name, email, passkey, address))
        
        mycursor.execute("SELECT LAST_INSERT_ID()")  
        last_id = mycursor.fetchone()[0]
        
        mycursor.execute("INSERT INTO account (ID, ACCOUNT_NUMBER, AMOUNT) VALUES (%s, %s, %s)", 
                         (last_id, account_number, 0))
        
        mydb.commit()
        print(f"Your account has been created successfully! Your account ID is: {last_id}")
        print(f"Your account number is: {account_number}")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        mydb.rollback()
def sign_in(mydb, mycursor):
    print("Welcome To Our Bank\nBe a step ahead in life")
    name = input("Enter the Full name: ")
    passkey = input("Enter the password: ")
    
    mycursor.execute("SELECT * FROM customers WHERE Name = %s AND PASSWORD = %s", (name, passkey))
    user = mycursor.fetchone()
    if user:
        print("You have successfully signed in")
        account_menu(mydb, mycursor, name)
    else:
        print("Please enter the correct details")

def account_menu(mydb, mycursor, name):
    while True:
        print("""Please Select the Option
            (1) ADD Amount
            (2) Debit Amount
            (3) Check Balance
            (4) More
            (5) Exit
        """)
        choice = input("Enter the Choice: ")
        if choice == "1":
            add_money(mydb, mycursor, name)
        elif choice == "2":
            debit_money(mydb, mycursor, name)
        elif choice == "3":
            balance(mycursor, name)
        elif choice == "4":
            More(mydb, mycursor, name)
        elif choice == "5":
            print(f"Thank you {name}, visit again")
            break
        else:
            print("Please try again")

def add_money(mydb, mycursor, name):
    print("Deposit your Money")
    amount = float(input("Enter the Amount to deposit: "))

    mycursor.execute("SELECT id FROM customers WHERE Name = %s", (name,))
    result = mycursor.fetchone()

    if result:
        account_id = result[0]
        mycursor.execute("UPDATE account SET AMOUNT = AMOUNT + %s WHERE ID = %s", (amount, account_id))
        mydb.commit()
        print(f"Deposit Amount {amount} successfully deposited")
    else:
        print("Account not found")

def debit_money(mydb, mycursor, name):
    print("Debit Your Amount")
    amount = float(input("Enter the Debit Amount: "))
    mycursor.execute("SELECT id FROM customers WHERE Name = %s", (name,))
    result = mycursor.fetchone()

    if result:
        account_id = result[0]
        mycursor.execute("SELECT AMOUNT FROM account WHERE ID = %s", (account_id,))
        current_balance = mycursor.fetchone()[0]
        
        if current_balance >= amount:
            mycursor.execute("UPDATE account SET AMOUNT = AMOUNT - %s WHERE ID = %s", (amount, account_id))
            mydb.commit()
            print(f"Debit Amount {amount} successfully withdrawn")
        else:
            print("Insufficient amount")
    else:
        print("Account not found")

def balance(mycursor, name):
    mycursor.execute("SELECT id FROM customers WHERE Name = %s", (name,))
    result = mycursor.fetchone()

    if result:
        account_id = result[0]
        mycursor.execute("SELECT AMOUNT FROM account WHERE ID = %s", (account_id,))
        balance = mycursor.fetchone()[0]
        print(f"Your Available balance is: {balance}")
    else:
        print("Account not found")

def More(mydb, mycursor, name):
    while True:
        print("""Please Select the Option
            (1) Change Name
            (2) Change Password
            (3) Change E-mail ID 
            (4) Back to Menu
        """)
        change = input("Enter the option: ")
        if change == "1":
            change_name(mydb, mycursor, name)
        elif change == "2":
            change_password(mydb, mycursor, name)
        elif change == "3":
            change_email(mydb, mycursor, name)
        elif change == "4":
            break
        else:
            print("Invalid choice. Please try again!")

def change_name(mydb, mycursor, old_name):
    new_name = input("Enter your new name: ")
    mycursor.execute("UPDATE customers SET Name = %s WHERE Name = %s", (new_name, old_name))
    mydb.commit()
    print("Name updated successfully")
    return new_name

def change_password(mydb, mycursor, name):
    new_password = input("Enter your new password: ")
    mycursor.execute("UPDATE customers SET PASSWORD = %s WHERE Name = %s", (new_password, name))
    mydb.commit()
    print("Password updated successfully")

def change_email(mydb, mycursor, name):
    new_email = input("Enter your new email: ")
    mycursor.execute("UPDATE customers SET Email = %s WHERE Name = %s", (new_email, name))
    mydb.commit()
    print("Email updated successfully")

def main():
    mydb = connect_to_database()
    if mydb is None:
        return
    
    mycursor = mydb.cursor()

    while True:
        print("""Welcome To Our Bank 
            Be a step ahead in life""")
        print("""Please Select the Option
            (1) Open Account
            (2) Sign in
            (3) Exit
        """)
        choice = input("Enter the Option: ")
        if choice == "1":
            sign_up(mydb, mycursor)
        elif choice == "2":
            sign_in(mydb, mycursor)
        elif choice == "3":
            print("Thank you for using our services. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
 
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    main()