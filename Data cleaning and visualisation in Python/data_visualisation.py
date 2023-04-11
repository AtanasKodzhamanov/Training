import matplotlib.pyplot as plt
import pandas as pd
customer_id, purchase_date, item_name, item_price
1, 2021-01-01, Widget A, 10.99
2, 2021-01-02, Widget B, 12.99
1, 2021-01-03, Widget C, 8.99
3, 2021-01-04, Widget A, 10.99
2, 2021-01-05, Widget A, 10.99

# Load data
data = pd.read_csv('data.csv')

# Group the data by customer id and sum the item prices
total_spending = data.groupby('customer_id')['item_price'].sum()

# Create a bar chart of the total spending
plt.bar(total_spending.index, total_spending.values)

# Set the axis labels and title
plt.xlabel('Customer ID')
plt.ylabel('Total Spending')
plt.title('Total Spending by Customer')

# Display the graph
plt.show()
