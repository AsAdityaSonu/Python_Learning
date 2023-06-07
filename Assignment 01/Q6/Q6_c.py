#WAP to create a list of 100 random numbers between 100 and 900. Count and print the: All prime numbers
import random

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

random_numbers = random.sample(range(100, 901), 100)

prime_numbers = []

for number in random_numbers:
    if is_prime(number):
        prime_numbers.append(number)

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))
