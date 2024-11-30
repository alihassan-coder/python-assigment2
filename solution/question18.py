# 18. Create a function that takes a string and counts the frequency of each character.

def count_character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


text = "hello world"
char_frequency = count_character_frequency(text)
print(char_frequency)
