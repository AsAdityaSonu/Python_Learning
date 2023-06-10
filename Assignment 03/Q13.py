import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Set the random seed for reproducibility
np.random.seed(42)

# Create a random dataset of 500 rows and 10 columns
dataset = pd.DataFrame()

# Columns 1 to 4: [-10, 10]
dataset[[f"col{i+1}" for i in range(4)]] = pd.DataFrame(np.random.uniform(-10, 10, size=(500, 4)))

# Columns 5 to 8: [10, 20]
dataset[[f"col{i+1}" for i in range(4, 8)]] = pd.DataFrame(np.random.uniform(10, 20, size=(500, 4)))

# Columns 9 to 10: [-100, 100]
dataset[[f"col{i+1}" for i in range(8, 10)]] = pd.DataFrame(np.random.uniform(-100, 100, size=(500, 2)))

# Apply K-Means clustering
def apply_kmeans(dataset):
    scaler = MinMaxScaler()
    scaled_dataset = scaler.fit_transform(dataset)

    distortions = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled_dataset)
        distortions.append(kmeans.inertia_)

    # Plot the distance metric graph
    plt.plot(K, distortions, marker='o')
    plt.xlabel('Number of clusters (K)')
    plt.ylabel('Distortion')
    plt.title('K-Means Clustering - Elbow Method')
    plt.show()

# Apply Hierarchical clustering
def apply_hierarchical(dataset):
    linked = linkage(dataset, 'ward')

    plt.figure(figsize=(10, 6))
    dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
    plt.title('Hierarchical Clustering - Dendrogram')
    plt.xlabel('Data Index')
    plt.ylabel('Distance')
    plt.show()

# Determine the optimal number of clusters and plot distance metric graph using each algorithm
apply_kmeans(dataset)
apply_hierarchical(dataset)
