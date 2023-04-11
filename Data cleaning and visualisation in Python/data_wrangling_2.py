import pandas as pd
job_title, company_name, job_description, salary_range
Software Engineer, ABC Inc., Seeking a software engineer with experience in Python and Java, $80, 000 -$120, 000
Data Analyst, XYZ Corp., Looking for a data analyst with experience in SQL and Tableau, $60, 000 -$90, 000
Marketing Manager, LMN Co., Seeking a marketing manager with experience in SEO and social media, $70, 000 -$100, 000
To make the data more useful, we can use data wrangling techniques to transform the data into a format that is easier to analyze. Here's an example of how we can use Python and the pandas library to do this:

python
Copy code

# Load data
data = pd.read_csv('data.csv')

# Split the salary range column into minimum and maximum salary columns
data[['min_salary', 'max_salary']
     ] = data['salary_range'].str.split('-', expand=True)

# Remove the salary range column
data.drop('salary_range', axis=1, inplace=True)

# Display the data
print(data)
In this example, we first load the data into a pandas DataFrame using the read_csv() function. We then use the str.split() function to split the salary range column into two columns, one for the minimum salary and one for the maximum salary. We use the expand = True parameter to create two new columns.

Next, we remove the salary range column using the drop() function, with axis = 1 indicating that we want to remove a column. Finally, we display the data using the print() function.

This is another example of how data wrangling can be used to transform and shape data into a format that is easier to analyze or visualize. There are many other techniques and libraries available for data wrangling in Python, including the pandas library and the numpy library.
