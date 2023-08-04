from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[2,3],[5,6]])
y = np.array([4,5])

model = LinearRegression(fit_intercept=False)
model.fit(x,y)
# print(model.coef_) # [-3.          3.33333333]

# 역행렬
tmp = np.linalg.inv(x)
# print(tmp)

# 단위행렬
xid = np.identity(2, np.int8)

# print(xid)
# [1 0]
# [0 1]

# 내적곱 np.dot()
a = [[3,4,5], [2,3,4]]
a = np.array(a) # 2행 3열
b = [[1,2], [5,8], [3, 6]]
b = np.array(b)
# print(a.shape, b.shape)
# print(np.dot(a, b))

v1 = [4,2]
v2 = [8,4]
V = np.array([v1, v2])
# print(V)
# print(np.linalg.det(V)) # 선형종속 # 0으로 역행렬이 존재하지 않음
# print('rank % d' % np.linalg.matrix_rank(V)) # rank 1이면 선형종속

# 역행렬이 존재하는 선형독립
v3 = [3, 0]
v4 = [0, -2]
S = np.array([v3, v4])
# print(S)
# print(np.linalg.det(S))
# print('rank % d' % np.linalg.matrix_rank(S)) # rank 2 이상이면 선형독립

# 정규화 벡터
v5 = [1, -2, 3]
# print(np.linalg.norm(v5, 1))
# print(np.linalg.norm(v5, 2))