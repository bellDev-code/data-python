from PIL import Image
from glob import glob # 폴더관리
import numpy as np
import matplotlib.pyplot  as plt

# arr = '1 2 3 4 5 6 7'.split(' ')
# print(arr)

# a = []
# a.append(1)
# a.append(2) # append 하나씩 추가
# print(a)

# 리스트는 곱 하거나 더하는 구조가 아니다.

w1, w2 = 3,2
w = [3, 2]
b = 5
xdata = [[90, 80], [100, 20], [10, 20], [20, 40]]
yhat = []
# range는 사용하지 않는다. (최대한)
# for i in range(4):
#     yhat.append(xdata[i][0] * w1 + xdata[i][1] * w2 + b)
# print(yhat)

for i in xdata:
    yhat.append(i[0]*w1+i[1]*w2+b)
# print(yhat)

# 행렬의 내적곱
xdata = np.array(xdata)
# xdata.shape # (4, 2)
temp = np.dot(xdata, w)+b, yhat
# print(temp)

arr = np.arange(15).reshape(3, 5)
arr = np.reshape(arr, (5,3))
# print(arr.shape) # 3,5
# print(arr)

# image 자료
fileList = glob('d:/data/img/*.jpg')
img = Image.open(fileList[0]).convert('RGB').resize((100,100))
np.shape(img) # 30행과 50열, 3채널 [r, g, b] (30, 50, 3)
imgArr = np.array(img)

# numpy array는 for문, if문 사용하지 않는다.
# imgArr[imgArr[:,:,:]>100] = 0

# 머신러닝 계산이 필요할때
# 저장할때 file 0 - 255로
plt.subplot(1,2,1)
plt.imshow(imgArr/255) # 연산을 위해서

plt.subplot(1,2,2)
plt.imshow(imgArr/127.5-1)
plt.show()