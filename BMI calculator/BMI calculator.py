

def calculate_BMI(weight,height):
    bmi = weight/(height**2)
    return bmi

 
def bmi_category(bmi):
    if bmi < 18.5:
        return "under weight"
    elif 18.5<= bmi <24.9:
        return "Normal weight"
    elif 25 <= bmi <29.9:
        return"over weight"
    else:
        return "obesity" 
def bmi_calculator():
    print("Welcome To The BMI Calculator")
    weight = float(input("Enter your weight in kilogram:"))
    height = float(input("enter your height in meters:"))
    bmi = calculate_BMI(weight,height)
    print(f'Your BMI is : {bmi:.2f}')
    print(f'Your BMI category is:{bmi_category(bmi)}')

bmi_calculator()
