# 6. Write a function to count the vowels in a given string.

uer_input = input("Enter a String : ")


def chack_string(uer_input):
    count = 0
    for chr in uer_input:
        if chr in "aeiou":
            count = count + 1
    return count

print(chack_string(uer_input))

