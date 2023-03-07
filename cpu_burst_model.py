import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

train_file = open("cpu_burst_training.csv", "r")
test_file = open("cpu_burst_testing.csv", "r")

training_data = pd.read_csv(train_file)
testing_data = pd.read_csv(test_file)


measured_column = 'pid'

train_X = training_data.drop(measured_column, axis=1)
train_y = training_data[measured_column]

test_X = testing_data.drop(measured_column, axis=1)
test_y = testing_data[measured_column]

rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)

rf_reg.fit(train_X, train_y)

y_predict = rf_reg.predict(test_X)

nse = mean_squared_error(y_predict, test_y)

print(nse)

