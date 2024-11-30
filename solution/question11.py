# 11. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

import math


num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))

gcd = math.gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is {gcd}")
