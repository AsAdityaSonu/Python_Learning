import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Create a random dataset of 100 rows and 30 columns
dataset = pd.DataFrame(np.random.randint(1, 201, size=(100, 30)))

# (i) Replace values with NA in the range [10, 60]
dataset.loc[10:60] = np.nan

# Print the count of rows with missing values
missing_rows_count = dataset.isna().sum(axis=1).sum()
print(f"Number of rows with missing values: {missing_rows_count}")

# (ii) Replace NA values with column averages
dataset = dataset.fillna(dataset.mean())

# (iii) Calculate Pearson correlation and plot heat map
correlation = dataset.corr()
sns.heatmap(correlation, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Pearson Correlation Heatmap")
plt.show()

# Select columns with correlation <= 0.7
selected_columns = correlation[correlation <= 0.7].dropna(axis=1).columns
print("Columns with correlation <= 0.7:")
print(selected_columns)

# (iv) Normalize values between 0 and 10
dataset = (dataset - dataset.min()) / (dataset.max() - dataset.min()) * 10

# (v) Replace values with 1 if <= 0.5, else with 0
dataset = dataset.applymap(lambda x: 1 if x <= 0.5 else 0)

# Print the updated dataset
print("Updated Dataset:")
print(dataset)
