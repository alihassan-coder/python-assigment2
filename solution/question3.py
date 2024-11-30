# 3. Write a function to find the factorial of a number using recursion

def factorial(n):
    if n < 0: 
        return "Undefined for negative numbers"
    result = 1
    for i in range(1, n + 1): 
        result *= i
    return result

print(factorial(8))  
