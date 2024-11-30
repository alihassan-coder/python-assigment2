# 4.  Write a function that takes a string and returns it reversed.

user_input = input("Enter a strainf : ")

def converter(user_input):
     user_input = user_input[ :: -1]
     print(user_input)

converter(user_input)