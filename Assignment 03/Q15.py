import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, wilcoxon, ttest_ind, ranksums

# Set the random seed for reproducibility
np.random.seed(42)

# Create a random dataset of 500 rows and 5 columns
dataset = pd.DataFrame(np.random.uniform(5, 10, size=(500, 5)), columns=[f"Column {i+1}" for i in range(5)])

# (i) Perform t-Test on each column
for column in dataset.columns:
    t_statistic, p_value = ttest_1samp(dataset[column], popmean=7.5)
    print(f"t-Test for {column}: t-statistic = {t_statistic:.4f}, p-value = {p_value:.4f}")

# (ii) Perform Wilcoxon Signed Rank Test on each column
for column in dataset.columns:
    statistic, p_value = wilcoxon(dataset[column] - 7.5)
    print(f"Wilcoxon Signed Rank Test for {column}: statistic = {statistic:.4f}, p-value = {p_value:.4f}")

# (iii) Perform Two Sample t-Test and Wilcoxon Rank Sum Test on Column 3 and Column 4
column_3 = dataset["Column 3"]
column_4 = dataset["Column 4"]

# Two Sample t-Test
t_statistic, p_value = ttest_ind(column_3, column_4)
print(f"Two Sample t-Test: t-statistic = {t_statistic:.4f}, p-value = {p_value:.4f}")

# Wilcoxon Rank Sum Test
statistic, p_value = ranksums(column_3, column_4)
print(f"Wilcoxon Rank Sum Test: statistic = {statistic:.4f}, p-value = {p_value:.4f}")
