import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#set random seed for reproducibility
np.random.seed(0)

#Class 1
mean1 = [2, 2]
cov1 = [[1, 0.5],[0.5, 1]]

X1 =np.random.multivariate_normal(mean1, cov1, 50)

#Class 2
mean2 = [6, 6]
cov2 = [[1, -0.3],[-0.3, 1]]
X2 = np.random.multivariate_normal(mean2, cov2, 50)

X = np.vstack(X1, X2)
Y = np.array([0] * 50 + [1] * 50)

plt.scatter(X1[:, 0], X2[:, 1], label='Class 0')
plt.scatter(X2[:, 0], X1[:, 1], lebel='Class 1')
plt.legend()
plt.title("Original Data")
plt.show()

lda = LinearDiscriminantAnalysis(n_components=1)
X_lda = lda.fit_transform(X, Y)

plt.scatter(X_lda[:50], np.zeros(50), label='CLass 0')
plt.scatter(X_lda[50:], np.zeros(50), label='CLass 1')
plt.legend()
plt.title("Data After LDA projection (1D)")
plt.show()
