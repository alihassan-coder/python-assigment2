# 13. Write a function that calculates the power of a number without using the ** operator.

num = int(input("Enter the number : "))
power = int(input("Enter the power of the number : "))

def power_of_number(num , power):
    result = 1
    for _ in range(power):
          result *= num
    return result

print(power_of_number(num , power))

     
