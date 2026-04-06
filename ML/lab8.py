import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=27)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=0)
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print("Accuracy score: ",accuracy_score(y_test, y_pred))

plt.figure(figsize=(20,10))

plot_tree(clf,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          rounded=True,
          precision=2)
plt.show()