import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = {
    'Age': [25, 30, 35, 40, 45, 45, 12, 65, 75, 87],
    'Salary': [50000, 60000, 70000, 80000, 90000, 90000, 30000, 100000, 110000, 120000],
    'Purchased': [0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['Age', 'Salary']]
y = df['Purchased']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#Build ANN model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=32,activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

#Compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Train 
print("Training the model...")
model.fit(X_train, y_train, epochs=50, batch_size=2, verbose=0)
print("Model training completed.")

#Evaluate
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy*100:.4f}%")

predictions = model.predict(X_test)

binary_predictions = (predictions > 0.5).astype(int)

for i in range(min(5, len(X_test))):
    print(f"Actual: {y_test.iloc[i]}, Predicted: {binary_predictions[i][0]}")