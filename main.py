import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'd:data/chipotle.tsv'

chipo = pd.read_csv(file_path, sep = '\t')

chipo.head(10)


# describe 함수로 요약 통계량 출력하기
# chipo['order_id'] = chipo['order_id'].astype(str)
# print(chipo.describe())

# print(len(chipo['order_id'].unique())) # order_id의 개수를 출력
# print(len(chipo['item_name'].unique())) # item_name의 개수를 출력

# 가장 많이 주문한 item
item_count = chipo['item_name'].value_counts()[:10]
# for idx, (a, b) in enumerate(item_count.items(), 1):
    # print("Top", idx, ":", a, b)

# best_item = chipo['item_name'].value_counts().index.tolist()[0]
# print(best_item)

# item당 주문 개수와 총량 구하기
order_count = chipo.groupby('item_name')['order_id'].count()
# print(order_count[:10])

item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10] #

item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

plt.bar(x_pos, order_cnt, align='center')
plt.ylabel('ordered_item_count')
plt.title('Distribution of all orderd item')

# plt.show()

