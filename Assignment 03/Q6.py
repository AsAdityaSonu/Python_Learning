import threading

def convert_to_uppercase(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Convert the content to uppercase
    content = content.upper()

    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Write the uppercase content back to the file
        file.write(content)

# Create a thread and pass the function along with the file name as arguments
thread = threading.Thread(target=convert_to_uppercase, args=('Aditya.txt',))

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()
