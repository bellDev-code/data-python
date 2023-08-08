import pandas as pd
from math import log
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    '먹고 싶은 사과',
    '먹고 싶은 바나나',
    '길고 노란 바나나 바나나',
    '저는 과일이 좋아요'
]

vocab = list(set(w for doc in docs for w in doc.split()))
# print(vocab)

# TF, IDF, 그리고 TF-IDF 값을 구하는 함수
N = len(docs) # 4

# TF
def tf(t, d):
    return d.count(t)

# IDF 역빈도수 : 단어(토픽)이 모든 문서에 골고루 출현되었는지 어떤 특정 문서에만 출현 되었는지 확인함.
def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
        return log(N/(df+1))

# TF-IDF
def rfidf(t, d):
    return rf(t,d)* idf(t)

# TF구하기
result = []
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tf(t, d))
        
tf_ = pd.DataFrame(result, columns=vocab)
# print(tf_)

# IDF 구하기
result = []
for j in range(len(vocab)):
    t = vocab[j]
    result.append(idf(t))
    
idf_ = pd.DataFrame(result, index=vocab, columns=["IDF"])
# print(idf_)

corpus = [
    'you know I want your love',
    'I like you',
    'what should I do ',
]

vecter = CountVectorizer()

print(vecter.fit_transform(corpus).toarray())

print(vecter.vocabulary_)