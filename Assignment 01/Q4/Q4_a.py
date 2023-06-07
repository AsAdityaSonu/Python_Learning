#print 100 random strings whose length between 6 and 8
import random
import string

random_strings = []
for i in range(100):
    length = random.randint(6, 8)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    random_strings.append(random_string)

for string in random_strings:
    print(string)
