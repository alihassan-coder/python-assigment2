def check_prime(n):
    if n <= 1:  
        print("The number is not prime")
        return

    for i in range(2, int(n**0.5) + 1):  
            print("The number is not prime")
            return

    print("The number is prime")


n = int(input("Enter the number: "))
check_prime(n)
