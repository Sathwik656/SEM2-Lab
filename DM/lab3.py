import pandas as pd

num_series = pd.Series([10,20,30,40,50])
str_series = pd.Series(["Apple","Banana","Cherry","Mango","Orange"])

#Convert series into list
num_list = num_series.tolist()
str_list = str_series.tolist()

print("Numeric Series: ",num_series)
print("Converted to List: ",num_list)

print("String Series: ",str_series)
print("Converted to List: ",str_list)