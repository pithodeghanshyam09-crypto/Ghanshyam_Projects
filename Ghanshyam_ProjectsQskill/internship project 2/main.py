import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/house_data.csv")

# Features and Target
X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict new house
new_house = pd.DataFrame(
    [[1600, 3, 2]],
    columns=['Size', 'Bedrooms', 'Bathrooms']
)

predicted_price = model.predict(new_house)
print("Predicted Price for new house:", predicted_price[0])
