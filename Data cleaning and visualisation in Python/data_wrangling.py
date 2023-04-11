import pandas as pd
Suppose we have a dataset that contains information about customers and their purchases, but the data is in a format that is difficult to analyze. The data looks like this:

yaml
Copy code
customer_id, purchase_date, item_name, item_price
1, 2021-01-01, Widget A, 10.99
2, 2021-01-02, Widget B, 12.99
1, 2021-01-03, Widget C, 8.99
3, 2021-01-04, Widget A, 10.99
2, 2021-01-05, Widget A, 10.99
To make the data more useful, we can use data wrangling techniques to transform the data into a format that is easier to analyze. Here's an example of how we can use Python and the pandas library to do this:

python
Copy code

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
In this example, we first load the data into a pandas DataFrame using the read_csv() function. We then use the pivot() function to transform the data into a format where each row represents a customer and each column represents an item, with the values being the prices of the items. We then fill any missing values with 0 using the fillna() function.

Next, we add a column for total spending by using the sum() function to sum the prices for each row. Finally, we sort the data by total spending using the sort_values() function, and display the data using the print() function.
