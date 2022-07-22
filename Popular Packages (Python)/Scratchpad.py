import pandas as pd

recipe = {
  "Flour": True,
  "Sugar": True,
  "Salt": False
}
series_dict = pd.Series(recipe)
print(series_dict)