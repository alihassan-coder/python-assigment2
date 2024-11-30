# 17. Write a function that takes a list and removes all duplicate elements.

def duplicate_remove(liste):
    liste.sort()  
    st = 0  
    end = 1  

    while end < len(liste):
        if liste[st] == liste[end]: 
            end += 1
        else: 
            st += 1
            liste[st] = liste[end]
    
    return liste[:st + 1]  

liste = [1, 3, 4, 5, 6, 4, 2]
print(duplicate_remove(liste))
