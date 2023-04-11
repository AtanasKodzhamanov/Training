import pandas as pd

customer_id, purchase_date, item_name, item_price
1, 2021-01-01, Widget A, 10.99
2, 2021-01-02, Widget B, 12.99
1, 2021-01-03, Widget C, 8.99
3, 2021-01-04, Widget A, 10.99
2, 2021-01-05, Widget A, 10.99


# Load data
data = pd.read_csv('data.csv')

# Pivot the data
data_pivoted = data.pivot(
    index='customer_id', columns='item_name', values='item_price')

# Fill missing values
data_pivoted.fillna(0, inplace=True)

# Add a column for total spending
data_pivoted['total_spending'] = data_pivoted.sum(axis=1)

# Sort by total spending
data_pivoted.sort_values(by='total_spending', ascending=False, inplace=True)

# Display the data
print(data_pivoted)
