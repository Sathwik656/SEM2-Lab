import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("cancer.csv")
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

scaler = StandardScaler() #Standardize the data
X_scaled = scaler.fit_transform(X)
print("Data before PCA: ")
print(X_scaled[0:2])

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(X_pca[0:2])

print("Explained variance: ", pca.explained_variance_ratio_)
print("Cumulative: ", np.cumsum(pca.explained_variance_ratio_))

plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:, 0],X_scaled[:, 1], c=y, cmap='coolwarn', edgecolor='k')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Original data (First two features)")
plt.colorbar(label='Diagnosis')
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarn', edgecolor='k')
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("PCA Transformed data")
plt.colorbar(label="Diagnosis")
plt.show()