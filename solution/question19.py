# 19. Write a function that takes a list of employee salaries and calculates the average salary.

def avrage_salaries(list):
    return sum(list) / len(list)

list = [ 3 , 4, 5,]
print(avrage_salaries(list))