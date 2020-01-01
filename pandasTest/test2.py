import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(np.random.randn(8, 3), index=index,columns=['A', 'B', 'C'])
print(s.array)#get acture data
print(df)