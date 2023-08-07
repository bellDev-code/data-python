import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'd:/data/drinks.csv'
drinks = pd.read_csv(file_path)

# print(drinks.info())

drinks.head(10)

# print(drinks.describe())
tmp = drinks.describe()
# 데이터프레임명['필드명']
# print(tmp['beer_servings'])
# tmp = drinks.describe().T
# print(tmp['count'])

# 피처간의 상관계수 행렬을 구합니다.
# 일반적으로 pearson 상관계수를 사용한다.
# -1은 음의 가장 큰 상관, 1은 양의 가장 큰 상관

# cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
cols = drinks.columns[1:5] # 위의 문장과 같다.
corr = drinks[cols].corr(method = 'pearson')
# print(corr)

cols_view = ['beer', 'spirit', 'wine', 'anchol']
sns.set(font_scale=1.5)
hm = sns.heatmap(corr.values,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 15},
                 yticklabels=cols_view,
                 xticklabels=cols_view)

plt.tight_layout()
plt.show()

sns.set(style='whitegrid', context='notebook')
sns.pairplot(drinks[['beer_servings', 'spirit_servings', 
                     'wine_servings', 'total_litres_of_pure_alcohol']], height=2.5)
# plt.show()

# print(drinks.isnull().sum())
# print("----------------------------")
# print(drinks.dtypes)

drinks['continent'] = drinks['continent'].fillna('OT')
# print(drinks.head(10))