#sort following number of elements in a list, calculate time taken and plot the graph.
import time
import matplotlib.pyplot as plt

#generate a list of specified size and measure the time taken to sort it
def sort_list(size):
    elements = list(range(size, 0, -1))  # Generate a list in descending order
    start_time = time.time()
    sorted_list = sorted(elements)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# Specify the numbers of elements in the list
sizes = [5000, 10000, 15000, 20000, 25000]

# Sort the lists and measure the time taken for each size
time_taken = []
for size in sizes:
    t = sort_list(size)
    time_taken.append(t)

# Print the time taken for each size
for i, size in enumerate(sizes):
    print(f"Number of elements: {size}, Time taken: {time_taken[i]} seconds")

# Plot the graph
plt.plot(sizes, time_taken, 'bo-')
plt.xlabel('Number of Elements')
plt.ylabel('Time taken (seconds)')
plt.title('Execution Time for Sorting')
plt.show()
