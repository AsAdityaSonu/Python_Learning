#Sum of Prime Numbers
L = [11, 12, 13, 14, 50, 60]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = sum(num for num in L if is_prime(num))
print(prime_sum)
