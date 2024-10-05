# using teh math Module
import math

number = int(input("Enter a number: "))
print(f"Factorial of {number} is :{math.factorial(number)}")

#using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")

# using loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")
  