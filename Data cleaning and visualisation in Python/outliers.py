import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('data.csv')

# Calculate z-scores
z_scores = np.abs(stats.zscore(data))

# Identify outliers
outliers = np.where(z_scores > 3)

# Remove outliers
data.drop(outliers[0], inplace=True)
# In this example, we use the numpy library to remove outliers from a dataset. We load the data from a CSV file, and then calculate the z-scores for each value in the dataset using the zscore() function. We then identify any values with a z-score greater than 3, which are considered outliers, and remove them using the drop() function.

# Overall, data cleaning is an essential step in any data analysis project, and there are many different techniques and libraries available for cleaning and processing data in Python, including pandas, numpy, and scipy.
