# for letter in ['A', 'B', 'C']:
    # print(letter)
    
# 원소뿐만이 아닌 index도 함께 출력하고 싶음
# i = 0
# for letter in ['A', 'B', 'C']:
    # print(i, letter)
    # i += 1

letters = ['A', 'B', 'C']
# for i in range(len(letters)):
    # letter = letters[i]
    # print(i, letter)
    
# 위의 방식은 파이썬답지 않은 코드라고 함
# for entry in enumerate(['A', 'B', 'C']):
    # print(entry)
# return 값이 튜플로 들어옴

# 인덱스와 원소를 다른 변수에 할당 unpacking
# for i, letter in enumerate(['A', 'B', 'C']):
    # print(i, letter)
# 시작 인덱스 변경
# for i, letter in enumerate(['A', 'B', 'C'], start=1):
    # print(i, letter)
    
# enumerate() 원리
iter_letters = iter(['A', 'B', 'C'])
# print(next(iter_letters))
# print(next(iter_letters))
# print(next(iter_letters))

enumerate_letters = enumerate(['A', 'B', 'C'])
# print(next(enumerate_letters))
# print(next(enumerate_letters))
# print(next(enumerate_letters))

# print(list(enumerate(['A', 'B', 'C'])))

# 2차원 리스트 루프
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

# for r in range(len(matrix)):
    # for c in range(len(matrix[r])):
        # print(r, c, matrix[r][c])

# 위와 동일한 코드
for r, row in enumerate(matrix):
    for c, letter in enumerate(row):
        print(r, c, letter)