#Sum of both the lists
import random

# Generate random lists
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

print("List 1:", list1)
print("List 2:", list2)

# Calculate sum of both lists
sum_list1 = sum(list1)
sum_list2 = sum(list2)

print("Sum of List 1:", sum_list1)
print("Sum of List 2:", sum_list2)
