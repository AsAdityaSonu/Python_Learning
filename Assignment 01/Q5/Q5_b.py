#Unique numbers in both the list
import random

# Generate random lists
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

print("List 1:", list1)
print("List 2:", list2)

# Find unique numbers in both lists
unique_numbers = list(set(list1) & set(list2))

print("Unique numbers in both lists:", unique_numbers)
