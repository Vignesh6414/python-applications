
number = str(int(input("Enter the number: ")))
sum_of_powers = 0
for i in number:
    sum_of_powers = sum_of_powers+int(i)**len(number)
    print(sum_of_powers)
    
if int(number) == sum_of_powers:
    print(f"{number},is an Armstrong Number.")
else:
    print(f"{number},is Not an ArmStrong Number.")
    