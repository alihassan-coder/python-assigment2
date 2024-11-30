# 9. Write a function to check whether a string is a palindrome.
user_input = input("Enter the string : ")

def chack_palindrome(user_input):
    revers_string = user_input[ :: -1]
    if revers_string == user_input:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

print(chack_palindrome(user_input))
