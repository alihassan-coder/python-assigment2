# 12. Create a function that accepts a dictionary and returns the key with the highest value.

def key_with_highest_value(d):
  
    if not d:
        return None  
    return max(d, key=d.get)

data = {"a": 10, "b": 20, "c": 15}
highest_key = key_with_highest_value(data)
print(f"The key with the highest value is '{highest_key}'")
