# 20.Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.


import random

def pass_genrater(leng):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
    lowercase = "abcdefghijklmnopqrstuvwzyz"
    num = "0987654321"
    special_char = "!@#$%^&*_-?"
    character = uppercase + lowercase + num + special_char
    
    password = ""
    for _ in range(leng):
        password += random.choice(character)
    return password

leng = int(input("Enter the len of password : "))
print(pass_genrater(leng))
    



