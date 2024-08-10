def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    x = 0
    for i in data.values():
        if i > x:
            x = i
    return x

data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }

print(find_max_value(data))