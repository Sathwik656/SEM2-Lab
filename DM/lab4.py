#Compare Elements of Two Pandas Series.

import pandas as pd

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,10])

print("Series 1 == Series 2",s1==s2)
print("\nSeries 1 > Series 2",s1>s2)
print("\nSeries 1 < Series 2",s1<s2)