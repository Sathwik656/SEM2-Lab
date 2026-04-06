import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("iris_dataset.csv")

print(data.head())

X=data.drop('variety',axis=1)
y=data['Variety']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regr = LinearRegression()
regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

print('Accuracy: ',accuracy_score(y_test,y_pred))

df = pd.DataFrame([{'sepal.length':4.2,'sepal.width':3.2,'petal.length':3.4,'petal.width':4.1}])

res = regr.predict(df)
print('Prediction: ',res)