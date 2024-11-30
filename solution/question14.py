# 14. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

temp = int(input("Enter the temperature : "))
scale = (input("Enter the scale C/F : "))

def temp_type_converter(temp , scale ):
    if scale == "C" :
        return (temp * 9/5) + 32 
    elif scale == "F":
        return (temp - 32 ) * 5 /9
    else:
        print("Enter the valid scale.")

print(temp_type_converter(temp , scale))
    