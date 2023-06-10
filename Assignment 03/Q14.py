import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Create a random dataset of 600 rows and 15 columns
dataset = pd.DataFrame(np.random.uniform(-100, 100, size=(600, 15)), columns=[f"Column {i+1}" for i in range(15)])

# (i) Scatter plot between Column 5 and Column 6
plt.scatter(dataset["Column 5"], dataset["Column 6"])
plt.xlabel("Column 5")
plt.ylabel("Column 6")
plt.title("Scatter Plot - Column 5 vs Column 6")
plt.show()

# (ii) Histogram of each column in a single graph
plt.figure(figsize=(10, 6))
for column in dataset.columns:
    plt.hist(dataset[column], bins=20, alpha=0.5, label=column)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Columns")
plt.legend()
plt.show()

# (iii) Box plot of each column in a single graph
plt.figure(figsize=(10, 6))
dataset.boxplot()
plt.title("Box Plot of Columns")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.show()
