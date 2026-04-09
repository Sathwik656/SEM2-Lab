#Program to create Mean, Median, Mode & SD from Data

import pandas as pd

data = input("Enter numbers separated by space: ")
num_list = list(map(int, data.split()))

series = pd.Series(num_list)

mean_val = series.mean()
median_val = series.median()
mode_val = series.mode()
std_val = series.std()

print("Mean: ", mean_val)
print("Median: ", median_val)
print("Mode: ", mode_val)
print("Standard Deviation: ", std_val)