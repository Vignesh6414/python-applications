from datetime import datetime
name = input("Enter your Birth day(dd-mm-yyyy): ")

date, month, year = map(int,name.split("-"))

today = datetime.today()
age = today.year-year-((today.month,today.day) <(month,date) )
print(age)
