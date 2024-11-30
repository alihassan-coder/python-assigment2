# 8. Write a function to find the nth Fibonacci number using recursion.

def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nth_fibonacci = 10
result = fibonacci(nth_fibonacci)
print(f"The {nth_fibonacci}th Fibonacci number is {result}")

