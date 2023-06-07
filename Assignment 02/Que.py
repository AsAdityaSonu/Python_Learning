#Write a python program to sort the list of heterogeneous data.
def sort_heterogeneous_data(data):
    # Separate 
    numbers = []
    strings = []
    booleans = []
    others = []

    for item in data:
        if isinstance(item, int) or isinstance(item, float):
            numbers.append(item)
        elif isinstance(item, str):
            strings.append(item)
        elif isinstance(item, bool):
            booleans.append(item)
        else:
            others.append(item)

    # Sort the individual lists
    numbers.sort()
    strings.sort()
    booleans.sort()
    others.sort()

    # Combine
    sorted_data = numbers + strings + booleans + others
    return sorted_data


data_list = [5, 'apple', True, 3.14, 'banana', False, 10, 'cherry']
sorted_list = sort_heterogeneous_data(data_list)
print(sorted_list)
