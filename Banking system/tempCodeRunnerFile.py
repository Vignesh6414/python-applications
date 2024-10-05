import mysql.connector
import hashlib
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Meenatchi2310",
  database="myBank"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myBank")
# mycursor.execute("CREATE TABLE customers (Name VARCHAR(255),Email VARCHAR(255),PASSWORD int,ADDRESS VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("ALTER TABLE customers ADD COLUMN MONEY INT ")
# mycursor.execute("ALTER TABLE customers DROP COLUMN MONEY")
# mycursor.execute("CREATE TABLE Account (ID INT AUTO_INCREMENT PRIMARY KEY,AMOUNT INT,ACCOUNT_NUMBER INT)")
# mycursor.execute("ALTER TABLE Account ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("ALTER TABLE Account ADD COLUMN Name VARCHAR(255)")
# mydb.commit()
# mydb.commit()


# for x in mycursor:
#     print(x)
Amount = []
    
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
        
        mycursor.execute("INSERT INTO customers (Name, Email, PASSWORD, ADDRESS) VALUES (%s, %s, %s, %s)", 
                         (name, email, hashed_password, address))
        
        
        customer_id = mycursor.lastrowid
        
        mycursor.execute("INSERT INTO account (customer_id, ACCOUNT_NUMBER, AMOUNT) VALUES (%s, %s, %s)", 
                         (customer_id, account_number, 0))
        
        mydb.commit()

        print(f"Your account has been created successfully! Your account ID is: {account_number}")

    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        mydb.rollback() 

def sign_in():
    print("""Welcome To Our Bank 
        Be a step ahead in life""")
    name = input("Enter the Full name: ")
    print()
    passkey = input("Enter the password: ")
    hashed_password = hash_password(passkey)

    mycursor.execute("SELECT id FROM customers WHERE Name = %s AND PASSWORD = %s", (name, hashed_password))
    result = mycursor.fetchone()

    if result:
        customer_id = result[0]
        print("Your successfully Sign in")
        account_menu(mydb, mycursor, name, customer_id)
    else: 
            print("please Enter the Correct Details")

def transfer_money(mydb, mycursor, sender_customer_id):
    receiver_name = input("Enter the Receiver name: ")
    mycursor.execute("SELECT Name FROM customers WHERE Name = %s", (receiver_name,))
    receiver_result = mycursor.fetchone()
    if not receiver_result:
        print("Receiver account not found.")
        return
    receiver_customer_id = receiver_result[0]
    mycursor.execute("SELECT id FROM customers WHERE Name = %s", (sender_customer_id,))
    sender_balance_result = mycursor.fetchone()
    if sender_balance_result:
        sender_balance = sender_balance_result[0]
        mycursor.execute("SELECT AMOUNT FROM account WHERE customer_id = %s", (sender_customer_id,))
        sender_balance = mycursor.fetchone()[0]


        amount = float(input("Enter the amount to transfer: "))

        if sender_balance >= amount:
            try:
                mydb.start_transaction()
                mycursor.execute("UPDATE account SET AMOUNT = AMOUNT - %s WHERE customer_id = %s", (amount, sender_customer_id))

                mycursor.execute("UPDATE account SET AMOUNT = AMOUNT + %s WHERE customer_id = %s", (amount, receiver_customer_id))

                mydb.commit()
                print(f"Successfully transferred {amount} to {receiver_name}")
            except mysql.connector.Error as err:
                print(f"An error occurred: {err}")
                mydb.rollback()
        else:
            print("Insufficient balance for transfer.")
    else:
        print("Your account not found.")


def account_menu(mydb, mycursor, name,customer_id):
    while  True:
        print(""" please Select the Option
            
            (1) ADD Amount
            (2) Debit Amount
            (3) Check Balance
            (4) Transfer money
            (5) More
            (6) Back to Main Menu
                    """)
        choice = int(input("Enter the Choice: "))
        if 1 == choice:
            add_money(mydb,mycursor, customer_id)
        elif 2 == choice:
            debit_money(mydb,mycursor, customer_id)
        elif 3 == choice:
            balance(customer_id)
        elif 4 == choice:
            transfer_money(mydb, mycursor, customer_id)
        elif 5 == choice:
            More(mydb, mycursor, name, )
        elif 6 == choice:
            print(f"Thank you {name} visit again")
            break
        else:
            print("pls try again")
        

# def add_money(mydb,mycursor,customer_id):

#     print("Deposit you Money")
#     Amount = int(input("Enter the Amount to deposit: "))

#     mycursor.execute("SELECT id FROM customers WHERE Name = %s", (customer_id,))
#     result = mycursor.fetchone()

#     if result:
#         account_id = result[0]
#         mycursor.execute("UPDATE account SET AMOUNT = AMOUNT + (%s) WHERE ID =(%s)",(Amount,account_id))
#         mydb.commit()
#         print(f"Deposit Amount{Amount} success fully Deposited")
#     else:
#         print("Account not fount")

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

# def debit_money(mydb,mycursor,customer_id):
    
#     print("Debit Your Amount")
#     Amount = float(input("Enter the Debit Amount: "))
#     mycursor.execute("SELECT id FROM customers WHERE Name =(%s)", (customer_id,))
#     result = mycursor.fetchone()

#     if result:
#         account_id = result[0]
#         mycursor.execute("SELECT AMOUNT FROM Account WHERE customer_id = %s", (customer_id,))
#         current_balance = mycursor.fetchone()[0]
        
#         if current_balance >= Amount:
#             mycursor.execute("UPDATE account SET AMOUNT = AMOUNT - (%s) WHERE customer_id = (%s)",(Amount,account_id))
#             mydb.commit()
#             print(f"Debit Amount {Amount} success fully withdraw")
#         else:
#             print("Insufficient amount")
#     else:
#         print("account not found.")

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
        SELECT a.AMOUNT, a.ACCOUNT_NUMBER 
        FROM Account a 
        WHERE a.customer_id = %s
    """, (customer_id,))
    result = mycursor.fetchone()

    if result:
        balance, account_number = result
        print(f"Your Account Number: {account_number}")
        print(f"Your Available balance is: {balance}")
    else:
        print("Account not found.")



def More(mydb, mycursor, name):
    while  True:
        print(""" please Select the Option
            
            (1) Change Name
            (2) change password
            (3) change E-mail ID 
            (4) Back to Menu
                    """)
        change = int(input("Enter the option: "))
        if 1 == change:
            change_name(mydb, mycursor, name)
        elif 2 == change:
            change_password(mydb, mycursor, name)
        elif 3 == change:
            change_email(mydb, mycursor, name)
        elif 4 == change:
            break
        else:
            print("Invalid choice. please try again!")


def change_name(mydb, mycursor, old_name):
    new_name = input("Enter your new name: ")
    mycursor.execute("UPDATE customers SET Name = (%s) WHERE Name = (%s)", (new_name, old_name))
    mydb.commit()
    print("Name updated successfully")


def change_password(mydb, mycursor, name):
    old_password = input("Enter the old password here: ")
    hashed_old_password = hash_password(old_password)
    mycursor.execute("SELECT * FROM customers WHERE Name = %s AND PASSWORD = %s", (name, hashed_old_password))
    if mycursor.fetchone():
        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password == confirm_password:
            hashed_new_password = hash_password(new_password)
            
            mycursor.execute("UPDATE customers SET PASSWORD = (%s) WHERE Name = (%s)", (hashed_new_password,name))
            mydb.commit()
            print("Password updated successfully")
        else:
            print("New passwords do not match. Password not updated.")
    else:
        print("Incorrect old password. Password not updated.")


def change_email(mydb, mycursor, name):
    new_email = input("Enter your new email: ")
    mycursor.execute("UPDATE customers SET Email = (%s) WHERE Name = (%s)", (new_email, name))
    mydb.commit()
    print("Email updated successfully")


def main():

    mycursor = mydb.cursor()

    while True:
        print("""Welcome To Our Bank 
            Be a step ahead in life""")
        print()
        print(""" please Select the Option
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
            print("Invalid choice. please try again.")
 
    mycursor.close()
    mydb.close()
if __name__ == "__main__":
    main()