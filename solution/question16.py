# 16. Create a function to check if two strings are anagrams.


input_string = input("Enter the first string : ")
input_2string = input("Enter the second string : ")

def chack_anagrams(input_string , input_2string ):
        if sorted(input_string) == sorted(input_2string):
            print("True")
        else:
            print("False")

print(chack_anagrams(input_string , input_2string))

