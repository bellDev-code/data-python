from string import ascii_lowercase as LOWERS

size = 10
arr = [0] * size
for i in range(size):
    arr[i] = i * 2

# print(arr)
# [ (변수를 활용한 값) for (사용할 변수 이름) in (순회할 수 있는 값)]
size = 10
arr = [n for n in range(1, 16) if n % 2 == 0 or n % 3 == 0]
# print(arr)

newarr = [n * n for n in arr]
# print(newarr)

word = '가나다'
# print([c * 2 for c in word])

# 2차원 매트릭스 4개의 행, 3개의 열
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

# print(len(arr))
# print(len(arr[0]))
# print(arr)
flat_one = [n for row in arr for n in row]
# print(flat_one)

flat_two = []
for row in arr:
    for n in row:
        flat_two.append(n)
# print(flat_two)

squared_list = [[n ** 2 for n in row] for row in arr]
# print(squared_list)

set_boy = {n ** 2 for n in range(10)}
# print(set_boy)

dict_boy = {c: n for c, n in zip(LOWERS, range(1, 27))}
# print(dict_boy)

# print(dict(zip(LOWERS, range(1, len(LOWERS)+1))))

tuple_boy = (n for n in range(1, 10))
# print(tuple_boy)

tuple_boy = tuple(n for n in range(1, 10))
# print(tuple_boy)