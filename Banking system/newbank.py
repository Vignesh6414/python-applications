import mysql.connector
import hashlib
import random
import logging
logging.basicConfig(level=logging.DEBUG)

# Then in your functions:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Meenatchi2310",
  database="dummy",
  autocommit=False

)

mycursor = mydb.cursor()

def setup_database():
    try:
        # Drop existing tables if they exist
        mycursor.execute("DROP TABLE IF EXISTS students")
        # mycursor.execute("DROP TABLE IF EXISTS customers")
        
        # Create customers table
        mycursor.execute("""
        CREATE TABLE customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            Email VARCHAR(255),
            PASSWORD VARCHAR(255),
            ADDRESS VARCHAR(255)
        )
        """)
        
        # Create account table with proper foreign key
        mycursor.execute("""
        CREATE TABLE account (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            ACCOUNT_NUMBER INT,
            AMOUNT INT DEFAULT 0,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
        """)
        
        mydb.commit()
        print("Database setup completed successfully")
    except mysql.connector.Error as err:
        print(f"An error occurred during database setup: {err}")
        mydb.rollback()

def hash_password(password):
    return hashlib.sha256(str(password).encode()).hexdigest()

def generate_account_number():
    return random.randint(10000, 99999)

def sign_up():
    print("Please fill your Details.") 
    name = input("Enter the Full name: ")
    email = input("Enter your email ID: ")
    password = input("Enter the password: ")
    address = input("Enter the Address: ")
    hashed_password = hash_password(password)
    
    account_number = generate_account_number()
    try:
        mydb.start_transaction()
        
        # Insert into customers first
        mycursor.execute("""
        INSERT INTO customers (Name, Email, PASSWORD, ADDRESS) 
        VALUES (%s, %s, %s, %s)
        """, (name, email, hashed_password, address))
        
        # Get the customer_id that was just created
        customer_id = mycursor.lastrowid
        
        # Now insert into account using the customer_id
        mycursor.execute("""
        INSERT INTO account (customer_id, ACCOUNT_NUMBER, AMOUNT) 
        VALUES (%s, %s, %s)
        """, (customer_id, account_number, 0))
        
        mydb.commit()
        print(f"Your account has been created successfully! Your account number is: {account_number}")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        mydb.rollback()

def sign_in():
    print("""Welcome To Our Bank 
        Be a step ahead in life""")
    name = input("Enter the Full name: ")
    passkey = input("Enter the password: ")
    hashed_password = hash_password(passkey)

    mycursor.execute("SELECT id FROM customers WHERE Name = %s AND PASSWORD = %s", (name, hashed_password))
    result = mycursor.fetchone()

    if result:
        customer_id = result[0]
        print("You've successfully signed in")
        account_menu(mydb, mycursor, name, customer_id)
    else: 
        print("Please enter the correct details")

# def transfer_money(mydb, mycursor, sender_customer_id):
#     receiver_name = input("Enter the receiver name: ")
#     mycursor.execute("SELECT id FROM customers WHERE Name = %s", (receiver_name,))
#     receiver_result = mycursor.fetchone()
    
#     if not receiver_result:
#         print("Receiver account not found.")
#         return
    
#     receiver_customer_id = receiver_result[0]
    
#     mycursor.execute("SELECT AMOUNT FROM account WHERE customer_id = %s", (sender_customer_id,))
#     sender_balance_result = mycursor.fetchone()
    
#     if sender_balance_result:
#         sender_balance = sender_balance_result[0]
#         amount = float(input("Enter the amount to transfer: "))

#         if sender_balance >= amount:
#             try:
#                 mydb.start_transaction()
                
#                 # Update sender's account
#                 mycursor.execute("""
#                 UPDATE account SET AMOUNT = AMOUNT - %s 
#                 WHERE customer_id = %s
#                 """, (amount, sender_customer_id))

#                 # Update receiver's account
#                 mycursor.execute("""
#                 UPDATE account SET AMOUNT = AMOUNT + %s 
#                 WHERE customer_id = %s
#                 """, (amount, receiver_customer_id))

#                 mydb.commit()
#                 print(f"Successfully transferred {amount} to {receiver_name}")
#             except mysql.connector.Error as err:
#                 print(f"An error occurred: {err}")
#                 mydb.rollback()
#         else:
#             print("Insufficient balance for transfer.")
#     else:
#         print("Your account not found.")

def transfer_money(mydb, mycursor, sender_customer_id):
    try:
        # First, check if receiver exists
        receiver_name = input("Enter the receiver name: ")
        mycursor.execute("SELECT id FROM customers WHERE Name = %s", (receiver_name,))
        receiver_result = mycursor.fetchone()
        
        if not receiver_result:
            print("Receiver account not found.")
            return
        
        receiver_customer_id = receiver_result[-1]
        
        # Check sender's balance
        mycursor.execute("SELECT AMOUNT FROM account WHERE customer_id = %s", (sender_customer_id,))
        sender_balance_result = mycursor.fetchone()
        
        if not sender_balance_result:
            print("Your account not found.")
            return
        
        sender_balance = sender_balance_result[0]
        amount = float(input("Enter the amount to transfer: "))

        if sender_balance < amount:
            print("Insufficient balance for transfer.")
            return
        
        # Start the transaction for the transfer
        
        # logging.debug(f"Starting transfer, sender balance: {sender_balance}")
        # Update sender's account
        mycursor.execute("""
        UPDATE account SET AMOUNT = AMOUNT - %s 
        WHERE customer_id = %s
        """, (amount, sender_customer_id))

        # Update receiver's account
        mycursor.execute("""
        UPDATE account SET AMOUNT = AMOUNT + %s 
        WHERE customer_id = %s
        """, (amount, receiver_customer_id))

        # Commit the transaction
        mydb.commit()
        print(f"Successfully transferred {amount} to {receiver_name}")
        
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        try:
            mydb.rollback()
        except mysql.connector.Error:
            pass  # If rollback fails, we've already rolled back

def account_menu(mydb, mycursor, name, customer_id):
    while True:
        print(""" Please Select the Option
            
            (1) Add Amount
            (2) Debit Amount
            (3) Check Balance
            (4) Transfer Money
            (5) More Options
            (6) Back to Main Menu
                    """)
        choice = int(input("Enter the Choice: "))
        if choice == 1:
            add_money(mydb, mycursor, customer_id)
        elif choice == 2:
            debit_money(mydb, mycursor, customer_id)
        elif choice == 3:
            balance(customer_id)
        elif choice == 4:
            transfer_money(mydb, mycursor, customer_id)
        elif choice == 5:
            more_options(mydb, mycursor, name)
        elif choice == 6:
            print(f"Thank you {name}, visit again")
            break
        else:
            print("Please try again")

def add_money(mydb, mycursor, customer_id):
    print("Deposit your Money")
    amount = int(input("Enter the Amount to deposit: "))

    try:
        mycursor.execute("""
        UPDATE account SET AMOUNT = AMOUNT + %s 
        WHERE customer_id = %s
        """, (amount, customer_id))
        mydb.commit()
        print(f"Deposit Amount {amount} successfully deposited")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        mydb.rollback()

def debit_money(mydb, mycursor, customer_id):
    print("Debit Your Amount")
    amount = float(input("Enter the Debit Amount: "))
    
    mycursor.execute("SELECT AMOUNT FROM account WHERE customer_id = %s", (customer_id,))
    current_balance = mycursor.fetchone()[0]
    
    if current_balance >= amount:
        try:
            mycursor.execute("""
            UPDATE account SET AMOUNT = AMOUNT - %s 
            WHERE customer_id = %s
            """, (amount, customer_id))
            mydb.commit()
            print(f"Debit Amount {amount} successfully withdrawn")
        except mysql.connector.Error as err:
            print(f"An error occurred: {err}")
            mydb.rollback()
    else:
        print("Insufficient balance")

def balance(customer_id):
    mycursor.execute("""
        SELECT AMOUNT, ACCOUNT_NUMBER 
        FROM account 
        WHERE customer_id = %s
    """, (customer_id,))
    result = mycursor.fetchone()

    if result:
        balance, account_number = result
        print(f"Your Account Number: {account_number}")
        print(f"Your Available balance is: {balance}")
    else:
        print("Account not found.")

def more_options(mydb, mycursor, name):
    while True:
        print(""" Please Select the Option
            
            (1) Change Name
            (2) Change Password
            (3) Change E-mail ID 
            (4) Back to Menu
                    """)
        change = int(input("Enter the option: "))
        if change == 1:
            change_name(mydb, mycursor, name)
        elif change == 2:
            change_password(mydb, mycursor, name)
        elif change == 3:
            change_email(mydb, mycursor, name)
        elif change == 4:
            break
        else:
            print("Invalid choice. Please try again!")

def change_name(mydb, mycursor, old_name):
    new_name = input("Enter your new name: ")
    try:
        mycursor.execute("UPDATE customers SET Name = %s WHERE Name = %s", (new_name, old_name))
        mydb.commit()
        print("Name updated successfully")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        mydb.rollback()

def change_password(mydb, mycursor, name):
    old_password = input("Enter the old password here: ")
    hashed_old_password = hash_password(old_password)
    
    mycursor.execute("SELECT * FROM customers WHERE Name = %s AND PASSWORD = %s", (name, hashed_old_password))
    if mycursor.fetchone():
        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password == confirm_password:
            hashed_new_password = hash_password(new_password)
            try:
                mycursor.execute("UPDATE customers SET PASSWORD = %s WHERE Name = %s", (hashed_new_password, name))
                mydb.commit()
                print("Password updated successfully")
            except mysql.connector.Error as err:
                print(f"An error occurred: {err}")
                mydb.rollback()
        else:
            print("New passwords do not match. Password not updated.")
    else:
        print("Incorrect old password. Password not updated.")

def change_email(mydb, mycursor, name):
    new_email = input("Enter your new email: ")
    try:
        mycursor.execute("UPDATE customers SET Email = %s WHERE Name = %s", (new_email, name))
        mydb.commit()
        print("Email updated successfully")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        mydb.rollback()

def main():
    try:
        setup_database()
        
        while True:
            print("""Welcome To Our Bank 
                Be a step ahead in life""")
            print()
            print(""" Please Select the Option
                        (1) Open Account
                        (2) Sign in
                        (3) Exit
                                """)
            choice = input("Enter the Option: ")
            if choice == "1":
                sign_up()
            elif choice == "2":
                sign_in()
            elif choice == "3":
                print("Thank you for using our services. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        mycursor.close()
        mydb.close()

if __name__ == "__main__":
    main()