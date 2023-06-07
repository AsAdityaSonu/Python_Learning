#WAP to create a list of 100 random numbers between 100 and 900. Count and print the: all the odd numbers
import random

# Generate random list
random_numbers = random.sample(range(100, 901), 100)

print("Random Numbers:", random_numbers)

# Count and print odd numbers
odd_numbers = [number for number in random_numbers if number % 2 != 0]

print("Odd Numbers:", odd_numbers)
print("Count of Odd Numbers:", len(odd_numbers))
