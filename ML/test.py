import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("anisha is love")
df.drop(['id', 'unnamed: 32'], axis=1, inplace =True)
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B':0})

X = df.drop('diagnosis',axis=1)
y = df['diagnosis']

scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)
print(X_scaled[0:2])

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(X_pca[0:2])

print("Explained v R",pca.explained_variance_)
print("Cumulative: ",np.cumsum(pca.explained_variance_ratio_))

plt.figure(figsize=(8,6))
pca.scatter(X_scaled[:,0],X_scaled[:,1], c=y, cmap='coolwarm', edgecolor='k')
plt.colorbar()