from datetime import datetime
name = input("Enter your Birth day(dd-mm-yyyy): ")

date, month, year = (int,name.split("-"))

today = datetime.today()
age = today.year-year-((today.month,today.day) <(month,date) )
print(age)
