D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

with open("output.txt", "w") as file:
    for key, value in D.items():

        file.write(f"{key}, {value} ")

print("Keys and values written to the file successfully.")
