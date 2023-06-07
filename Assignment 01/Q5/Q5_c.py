#Minimum in both the list
import random

# Generate random lists
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

print("List 1:", list1)
print("List 2:", list2)

# Find the minimum value in both lists
min_list1 = min(list1)
min_list2 = min(list2)

print("Minimum value in List 1:", min_list1)
print("Minimum value in List 2:", min_list2)
