#print all numbers between 100 and 1000 that are divisible by 7 and 9
start = 100
end = 1000

divisible_numbers = []

for number in range(start, end + 1):
    if number % 7 == 0 and number % 9 == 0:
        divisible_numbers.append(number)

print("Numbers between", start, "and", end, "divisible by 7 and 9:")
for divisible_number in divisible_numbers:
    print(divisible_number)
