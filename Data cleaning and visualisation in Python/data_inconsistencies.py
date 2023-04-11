import pandas as pd

# Load data
data = pd.read_csv('data.csv')

# Convert all strings to lowercase
data = data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
# In this example, we use the pandas library to handle inconsistent data in a dataset. We load the data from a CSV file, and then use the apply() function to convert all string values to lowercase. This is useful if the data contains inconsistent capitalization, which can make it difficult to search or analyze the data effectively.
