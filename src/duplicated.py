import pandas as pd
idx = ['row1', 'row2', 'row3', 'row4', 'row5']
col = ['col1', 'col2', 'col3']
data = [['A', '가', 1], ['A', '가', 1], ['A', '나', 2], ['A', '나', 3], ['B', '다', 4]]

df = pd.DataFrame(data, idx, col)

print(df)
print("///////")
print(df.duplicated())