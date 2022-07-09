import numpy as np
import pandas as pd
from numpy.random import randn


# 1. Series 
# Similar to NumPy's arrays but can be given a named or datetime index

labels = ["a","b","c"]
my_list=[10,12,14]
arr=np.array([10,20,30])
d={"a":100,"b":200}

print(pd.Series(my_list, index=labels)) # applies labels to my_list values
print(pd.Series(arr, index=labels))
print(pd.Series(d))
print(pd.Series(data=labels))

# 2. DataFrames

df=pd.DataFrame(randn(5,4),["A","B","C","D","E"],["W","X","Y","Z"])
print(df)
print(df["W"])

df["new"]=df["W"]+df["X"]
df.drop("new", axis=1) # does not happen in place. Set inplace=True
df.shape # returns dimensions
df.loc["A"] # returns a row
df.iloc[0] # returns row by position
print(df.loc[["A","B"],["W","Y"]]) # selects only these rows and cols