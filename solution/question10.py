# 10. Create a function that takes a list of integers and returns the sum of all even numbers.

array = [3 , 4 , 6 , 7 , 3 , 6 ]


def even_sum(array):
    cur_sum = 0
    for num in array:
        if num % 2 == 0 :
            cur_sum = cur_sum + num
    return cur_sum
           
print(even_sum(array))