import math

# Function to display menu options
def show_menu():
    print("\nScientific Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Exponent (x^y)")
    print("7. Logarithm (base 10)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Exit")

# Function to handle the user's choices and perform calculations
def scientific_calculator():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-11): ")

        # Perform selected operation
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")

        elif choice == '5':
            num = float(input("Enter the number: "))
            if num < 0:
                print("Error! Cannot calculate square root of a negative number.")
            else:
                print(f"Result: √{num} = {math.sqrt(num)}")

        elif choice == '6':
            base = float(input("Enter the base number (x): "))
            exponent = float(input("Enter the exponent (y): "))
            print(f"Result: {base}^{exponent} = {math.pow(base, exponent)}")

        elif choice == '7':
            num = float(input("Enter the number: "))
            if num <= 0:
                print("Error! Logarithm undefined for non-positive numbers.")
            else:
                print(f"Result: log10({num}) = {math.log10(num)}")

        elif choice == '8':  # Sine
            angle = float(input("Enter the angle in degrees: "))
            radians = math.radians(angle)
            print(f"Result: sin({angle}°) = {math.sin(radians)}")

        elif choice == '9':  # Cosine
            angle = float(input("Enter the angle in degrees: "))
            radians = math.radians(angle)
            print(f"Result: cos({angle}°) = {math.cos(radians)}")

        elif choice == '10':  # Tangent
            angle = float(input("Enter the angle in degrees: "))
            radians = math.radians(angle)
            print(f"Result: tan({angle}°) = {math.tan(radians)}")

        elif choice == '11':
            print("Exiting the Scientific Calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (1-11).")

# Run the scientific calculator
scientific_calculator()

