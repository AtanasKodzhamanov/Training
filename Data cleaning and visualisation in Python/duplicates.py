import pandas as pd

# Load data
data = pd.read_csv('data.csv')

# Check for duplicates
duplicates = data.duplicated()
print(f"Number of duplicates: {duplicates.sum()}")

# Remove duplicates
data.drop_duplicates(inplace=True)
# In this example, we use the pandas library to remove duplicates from a dataset. We load the data from a CSV file, and then use the duplicated() function to identify any rows that are duplicates. We then drop the duplicates using the drop_duplicates() function.
