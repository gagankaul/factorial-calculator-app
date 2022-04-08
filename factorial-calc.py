#Factorial Calculator App

import math

print("Welcome to the Factorial Calculator App.\n")

#Getting user input
num = int(input("What number would you like to compute the factorial of? "))

#Display the mathematical relationshiip of a factorial
print(f"{num}! = ", end = '')
for i in range (1, num):
    print(str(i), end=" * ")
print(str(num))

#Display result from math library
num_factor = math.factorial(num)

print("\nHere is the result from the math library:")
print("The factorial of " + str(num) + " is " + str(num_factor) + ".")

#Calculate and display result from algorithm
num_factor = 1
for i in range(1,num+1):
    num_factor *= i

print("\nHere is the result from my own algorithm:")
print(f"The factorial of {num} is {num_factor}")

print(f"\nIt is shown twice that {num}! = {num_factor} (with excitement)")
