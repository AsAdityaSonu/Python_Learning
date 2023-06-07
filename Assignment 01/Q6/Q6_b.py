#WAP to create a list of 100 random numbers between 100 and 900. Count and print the: All even numbers
import random

random_numbers = random.sample(range(100, 901), 100)
even_numbers = []

for number in random_numbers:
    if number % 2 == 0:
        even_numbers.append(number)

even_count = len(even_numbers)

print("List of Random Numbers:", random_numbers)
print("Even Numbers:", even_numbers)
print("Count of Even Numbers:", even_count)
