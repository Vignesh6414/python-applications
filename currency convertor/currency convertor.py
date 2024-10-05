conversion_rates = {
    "USD" : {"INR" : 82.50, "EUR" : 0.94, "GBR" : 0.79},
    "INR" : {"USD" : 0.012, "EUR" : 0.011, "GBR" : 0.0095},
    "EUR" : {"USD" : 1.06, "INR" : 88.00, "GBR" : 0.85},
    "GBR" : {"USD" : 1.27, "INR" : 103.50, "EUR" : 1.18}
   
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        rate = conversion_rates[from_currency][to_currency]
        return amount * rate
    else:
        return None
    
def currency_converter():
    print("welcome to the currency convertor!")
    print("Available currencies: USD, INR, EUR, GBR")

    from_currency = input("enter the currency you want to convert from (e.g., USD, INR) : ").upper()
    to_currency = input("enter the currency you want to convert to (e.g.,USD,INR) : ").upper()

    try:
        amount = float(input(f"Enter the Amount in {from_currency} : "))

        result = convert_currency(amount, from_currency, to_currency)
        if result:
            print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

        else:
            print("Conversion rate not available for the selected currencies.")

    except ValueError:
        print("Invalid input. Please enter a valid amount.")
currency_converter()

