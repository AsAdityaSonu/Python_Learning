import random
import string

with open("output9.txt", "w") as file:
    for _ in range(100):
        string_length = random.randint(10, 15)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=string_length))
        file.write(random_string + "\n")

print("Random strings written to the file successfully.")
