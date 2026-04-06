import pandas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pandas.read_csv("car.csv")
X = df[['Volume','Weight']]
y = df['C02']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regr = LinearRegression()
regr.fit(X_train, y_train)

#predict the C02 emission of a car where the weight is 2300kg, and the volume is 1300cm
predictedC02 = regr.predict([[2300,1300]])
print('Predicted C02: ',predictedC02)