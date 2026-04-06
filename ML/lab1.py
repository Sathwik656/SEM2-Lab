import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Linear regression plot
X = [2,4,6,2,4,7,9,7,8,9]
Y = [45,23,67,89,56,45,78,34,75,95]

slope, intercept, r, p, std_err = stats.linregress(X, Y)

def myfun(x):
    return slope * x + intercept

mymodel = list(map((myfun), X))
plt.scatter(X, Y)
plt.title('Linear Regression')
plt.plot(X, mymodel)
plt.show()

#Polynomial regression plot
x = [2,4,6,2,4,7,9,7,8,9]
y = [45,23,67,89,56,45,78,34,75,95]

mymodel = np.poly1d(np.polyfit(x, y, 2))
myline = np.linspace(1, 22, 100)
plt.scatter(x, y)
plt.title('Polynomial Regression')
plt.plot(myline, mymodel(myline))
plt.show()