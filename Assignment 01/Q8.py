L = ["One", "Two", "Three", "Four", "Five"]

with open("out.txt", "w") as file:
    for element in L:
        length = len(element)
        file.write(f"{element}, {length} ")

print("Element lengths written to the file successfully.")
