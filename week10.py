import pandas as pd

df1 = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8]}, index=[1, 2, 3])
df2 = pd.DataFrame({'국':[1, 3, 7], '수':[3, 5, 9]}, index=[1, 2, 3])
print(pd.merge(df1, df2, how='left', on = '국'))