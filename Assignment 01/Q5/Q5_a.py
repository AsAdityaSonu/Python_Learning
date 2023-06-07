#create two lists of 10 random numbers between 10 and 30
import random

# Generate random lists
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

print("List 1:", list1)
print("List 2:", list2)

# Find common elements
common_elements = list(set(list1) & set(list2))

print("Common elements:", common_elements)
