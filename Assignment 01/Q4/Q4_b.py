#print all prime numbers between 600 and 800
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

start = 600
end = 800

prime_numbers = []

for number in range(start, end + 1):
    if is_prime(number):
        prime_numbers.append(number)

print("Prime numbers between", start, "and", end, ":")
for prime_number in prime_numbers:
    print(prime_number)
