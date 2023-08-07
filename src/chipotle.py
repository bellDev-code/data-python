import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1년 동안 고객이 주문한 오더 자료
# q) 어떤 메뉴가 가장 많은 매출일까?
file_name = 'd:/data/chipotle.tsv'
chipo = pd.read_csv(file_name, sep='\t')
# print(chipo)

# pandas 행과 열의 개수를 파악해야한다.
# print(chipo.shape) # 4622, 5chipo.info()

# chipo.info()
# print(chipo.columns)

# 데이터 형(type)변환
# int: 정수, float: 소수점, object: 문자열

# chipo.astype({'order_id': float})
chipo['order_id'] = chipo['order_id'].astype(str)
# print(chipo.describe())

# item_price의 $ 표시 치환 '$2.39' 형태
# matplot에서 x축과 y축의 값은 항상 int 값 이여야 한다.
# chipo['item_price'] = chipo['item_price'].str.replace('$', '') # 문자열 형태로 변환되어 문제 발생
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:])) # 수정 코드
# print(chipo['item_price'])
# print(chipo['item_name'][:5])

# pandas 문자열 분리
chipo['item_group'] = chipo['item_name'].str.split(' ').str[0]
# print(chipo['item_group'])

# print(len(chipo['order_id'].unique()))
# print(len(chipo['item_name'].unique()))

# 전처리 완료
# print(chipo.head(10))
# print(chipo.isna().sum())

# 산점도
# plt.figure(figsize=(10, 3))
# plt.subplot(1,2,1) # 1줄(행), 2열 중 첫 번째 위치
# x = chipo.index
# y = chipo['quantity']
# plt.scatter(x, y)
# plt.title('scatter:quantity')

# plt.subplot(1,2,2) # 1줄(행), 2열 중 두 번째 위치
# y = chipo.item_price
# plt.scatter(x, y)
# plt.title('scatter:item_price')

# list_ = ['quantity', 'item_price']
# for i, column in enumerate(list_, 1):
#     plt.subplot(1, 2, i)
#     x = chipo.index
#     y = chipo[column]
#     plt.scatter(x, y)

# plt.show()

# 가장 많이 주문한 item : 10등까지
item_count = chipo['item_name'].value_counts()[:10]
# for idx, (val, cnt) in enumerate(item_count.items(), 1):
#     print("Top", idx, ":", val, cnt)

# 가장 많이 주문한 item
top_name = chipo['item_name'].value_counts().index.tolist()[0]
# print(top)

# groupby란
group_size = chipo.groupby('item_group').size()
# print(group_size)
# print(group_size / group_size.sum() * 100)
# print(type(group_size), type(chipo)) # <class 'pandas.core.series.Series'> <class 'pandas.core.frame.DataFrame'>

# plt.barh(group_size.index, group_size)
# plt.show()

# item_group의 item_price 총합
group_count = chipo.groupby('item_group')['item_price'].sum()
# plt.barh(group_count.index, group_count)
# plt.show()


