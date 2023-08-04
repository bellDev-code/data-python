import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_path = 'd:/data/'
aisles = pd.read_csv(base_path + 'aisles.csv')
departments = pd.read_csv(base_path + "departments.csv")
prior = pd.read_csv(base_path + "order_products__prior.csv")
train = pd.read_csv(base_path + "order_products__train.csv")
orders = pd.read_csv(base_path + "orders.csv")
products = pd.read_csv(base_path + "products.csv")

prior_sample = prior[:10000]
# print(prior_sample)

temp = pd.merge(orders, prior_sample, on="order_id")
temp = pd.merge(temp, products, on="product_id")
temp = pd.merge(temp, aisles, on="aisle_id")
temp = pd.merge(temp, departments, on="department_id")

# print(temp)

# EDA
# 위의 코드에서 가져온 1만개의 거래내역에 대해서 각 물품을 얼마나 샀을까?
# user = temp.user_id.value_counts() # 972명의 고객
# product = temp.product_name.value_counts() # banana 4511개의 product
# asi = temp.aisle.value_counts() # fresh fruits 1128
# temp.department.value_counts() # produce 2913
# temp.order_dow.value_counts() # 1 2135
# temp.order_hour_of_day.value_counts()

# 데이터 전처리
