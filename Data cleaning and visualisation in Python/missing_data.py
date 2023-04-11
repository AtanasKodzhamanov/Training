import pandas as pd

# Load data
data = pd.read_csv('data.csv')

# Check for missing values
missing = data.isnull().sum()
print(f"Number of missing values:\n{missing}")

# Replace missing values with the mean
mean = data.mean()
data.fillna(mean, inplace=True)

# In this example, we use the pandas library to handle missing data in a dataset. We load the data from a CSV file, and then use the isnull() function to identify any rows that contain missing values. We then calculate the mean of each column, and replace the missing values with the mean using the fillna() function.
