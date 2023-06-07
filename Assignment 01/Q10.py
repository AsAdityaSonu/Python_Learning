def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

with open("output10.txt", "w") as file:
    #prime numbers between 600 and 800 to the file
    for number in range(600, 801):
        if is_prime(number):
            file.write(str(number) + "\n")

print("Prime numbers written to the file successfully.")
