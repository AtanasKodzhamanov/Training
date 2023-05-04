import numpy as np
import pandas as pd
from numpy.random import randn


# 1. Series 
# Similar to NumPy's arrays but can be given a named or datetime index
# list -> series -> dataframe

labels = ["a","b","c"]
my_list=[10,12,14]
arr=np.array([10,20,30])
d={"a":100,"b":200}

print(pd.Series(my_list, index=labels)) # applies labels to my_list values
print(pd.Series(arr, index=labels))
print(pd.Series(d)) # creates a series from the dictionary keys and values
print(pd.Series(data=labels))
series=pd.Series(my_list, index=labels)
#some methods you can apply to series
# .sum() .mean() .std() .max() .min() .argmax() .argmin() .value_counts() .apply() .sort_values() .isnull()

# Attributes of series
# .index .values .dtype .shape .size .name .is_unique .ndim .axes .empty .hasnans .str 

# Series parameters

pd.Series(
    data=None, # data to be stored in the series
    index=None, # index labels
    dtype = None, # data type
    name= None, # name of the series
    copy: bool = False, # copy data
    fastpath: bool = False, # internal
)

# Import csv file as a dataframe
pd.read_csv("filename", usecols = ["colname"]).squeeze() # squeeze() converts dataframe column to series

series.sort_values(ascending=True) # sorts series in ascending order

10 in series.values # checks if 10 is in series. If you don't put .values, it will check if 10 is in the index

# some standard operations on lists also work on series 
# negative indexing works on series but you need to add both values -20:-10
# you can also use the index label to fitler the series series["label"]

# 2. DataFrames

pd.read_csv("filename", parse_dates=["colname","col"]) # converts column to datetime

df=pd.DataFrame(randn(5,4),["A","B","C","D","E"],["W","X","Y","Z"])
df.info() # returns info about the dataframe

print(df)
print(df["W"])

df["new"]=df["W"]+df["X"]
df.drop("new", axis=1) # does not happen in place. Set inplace=True
df.shape # returns dimensions
df.loc["A"] # returns a row
df.iloc[0] # returns row by position
print(df.loc[["A","B"],["W","Y"]]) # selects only these rows and cols

df["Gender"].astype("category") # converts column to category which is more efficient than storting strings

df["Gender"].value_counts() # returns the number of times each value appears in the column
df["Gender"].value_counts(normalize=True)*100 # returns the percentage of times each value appears in the column
df.dropna() # drops rows with missing values 
df.dropna(how = "all") # drops rows where all values are missing. you can also specify "any"
df.dropna(subset=["col1","col2"]) # drops rows where col1 or col2 are missing
df.fillna(0) # fills missing values with 0. But this does not happen in place. Set inplace=True to make it happen in place (i.e. change the dataframe)

# 3. Filtering dataframes

# Essentially pass true/false values to the dataframe to filter out rows that are false
df[df["Gender"]=="Male"]
df[df["Salary"]>100000]

mask = df["Team"]=="Marketing"
df[mask]

df["Team"].isin(["Marketing","Finance"]) # returns true/false values for each row

# Can also use multiple conditions with & and | operators

mask = df["Team"].isin("Legal","Sales")

df["Name"].sort_values() # sorts the column in ascending order
df.sort_values(by=["Name","Town"], ascending=False) # sorts the dataframe by the column
df["Salary"].rank(ascending=False) # returns the rank of each value in the column in descending order (i.e. highest value has rank 1) 
df[df["Salary"].between(60000,70000)] # returns rows where salary is between 60000 and 70000

df["Name"].duplicated(keep=True) # returns true/false values for each row. True if the name is duplicated (i.e. appears more than once). It marks the first occurence as False and the rest as True.

# 4. GroupBy

sectors=df.groupby("Sector") # returns a groupby object. You can also group by multiple columns by passing a list of column names
sectors.size() # returns the number of rows in each group
sectors.groups() # returns a dictionary with the groups and the rows in each group as a list of indices 
sectors.get_group("Energy") # returns the rows in the group

# You can also apply min max mean sum etc to the groupby object to get the min max mean sum of each group. So if the dataset has 5 columns and you apply min, you will get the min of each column for each group. Or you can specify a column to apply the function to:

sectors["Revenue"].sum() # returns the sum of the revenue column for each group

# agg() method allows you to apply multiple functions to the groupby object
sectors.agg() # returns the sum of each column for each group 
sectors.agg({"Revenue":["sum","mean"],"Employees":"mean"}) # returns the sum of revenue and mean of employees for each group


# 5. Merging, Joining and Concatenating