import pandas as pd

# Load the dataset
cars = pd.read_csv('cars.csv', index_col=0)

# Display single row
print(cars.loc['JAP'])

# Display multiple rows
print(cars.loc[['AUS', 'EG']])

# Access specific cell value
print(cars.loc['MOR', 'drives_right'])

# Display sub-DataFrame with specific rows and columns
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
