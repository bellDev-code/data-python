import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from func.func import quali_cnt

file_path = 'd:/data/bank.csv'

df = pd.read_csv('d:/data/bank.csv', sep=',')
# df.info()

# quali_cnt(df, 'age')

# plt.figure(figsize=(10, 3))
# plt.subplot(1, 2, 1)
# data1 = np.random.normal(size=1000)
# plt.hist(data1, bins=10)
# print(data1.std(), data1.mean()) # std() = 모집단 추출(n) / 표본집단 (n-1)

# plt.subplot(1,2,2)
# data2 = np.random.random(size=1000)
# plt.hist(data2, bins=10)
# print(data2.std(), data2.mean())

# numpy std option
# ddof = 0 모집단, ddof = 1 표본집단
# pandas std ddof=1 기본값

def scatters(data, h=None, pal=None):
    fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(8,8))
    sns.scatterplot(x="campaign",y="duration", hue=h, palette=pal, data=data, ax=ax1)
    sns.scatterplot(x="age",y="campaign", hue=h, palette=pal, data=data, ax=ax2)
    sns.scatterplot(x="age",y="duration", hue=h, palette=pal, data=data, ax=ax3)
    plt.tight_layout()
    
scatters(df, h="marital")


# plt.show()

data = '''221,305,440,275,190,330,200,317,371,350,255,318,280,277,330,230,260,175,285,175,300,416,240,320,390,150,250,210,490, 318'''

a = []
for x in data.split(','):
    a.append(int(x))
# print(a)

# list comprehension
data = [int(x) for x in data.split(',')]
# print(data[:3])

x, y, z = np.mean(data), np.median(data), np.std(data, ddof=1)
# print(x,y,z)

# https://www.kaggle.com/code/hamelg/python-for-data-24-hypothesis-testing