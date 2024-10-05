import random
import string

def random_code (length=2):
    number = string.digits
    code = '' .join(random.choice(number) for _ in range(length)) 
    return code
random_code_gen = random_code()
print(f"Random Code: {random_code_gen}")        