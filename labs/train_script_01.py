import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# load the tft matches dataset
print("Loading Data...")
diabetes = pd.read_csv('./tft_matches.csv')

# separate features and labels
X, y = diabetes[['level','gold_left','total_damage_to_players','num_units']].values, diabetes['level'].values

# split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# train a linear regression model
print('Training a linear regression model')
model = LinearRegression()
model.fit(X_train, y_train)

# calculate error
print('Calculating error...')
y_pred = model.predict(X_test)
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))