#Maximum in both the list
import random

# Generate random lists
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

print("List 1:", list1)
print("List 2:", list2)

# Find maximum values
max_value_list1 = max(list1)
max_value_list2 = max(list2)

print("Maximum value in List 1:", max_value_list1)
print("Maximum value in List 2:", max_value_list2)
