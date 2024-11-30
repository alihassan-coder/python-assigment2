# 7. Create a function that takes a list of numbers and returns the largest number.

array = [3 , 65,788, 8,994, 54,5 ]

def findLargeNamber(array):
    array2 = sorted(array)
    return array2[-1]

print(findLargeNamber(array))