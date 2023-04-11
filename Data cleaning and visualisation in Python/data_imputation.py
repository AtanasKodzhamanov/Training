import pandas as pd
from sklearn.impute import SimpleImputer

# Load data
data = pd.read_csv('data.csv')

# Impute missing values with the median
imputer = SimpleImputer(strategy='median')
data_imputed = imputer.fit_transform(data)
# In this example, we use the sklearn library to impute missing data in a dataset. We load the data from a CSV file, and then use the SimpleImputer() function to impute missing values with the median value for each column. This is useful if the data contains missing values, which can make it difficult to analyze the data effectively.
