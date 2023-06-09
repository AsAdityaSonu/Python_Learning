#Convert all the files of question 4 to uppercase
import random as r
import string as s

file_size= 5*1024*1024

# Open the file for reading
with open('Aditya.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()

# Convert each string to uppercase
updated_contents = [line.upper() for line in contents]

# Open the same file for writing
with open('Aditya.txt', 'w') as file:
    # Write the updated contents to the file
    file.writelines(updated_contents)

file.close()
