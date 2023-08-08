from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

cand_mask=np.array(Image.open('d:/data/img/circle.png'))

words = {
    'domdom':1666,
    '티스토리':955,
    '돔돔':855,
    '워드':841,
    '클라우드':612,
    '파이썬':598,
    'tistory':576,
    '코딩':542,
    '장인':487,
    '블로그':412,
    '방문자':401,
    '댓글':397,
    '롤':391,
    '칼바람':308,
    '나락':284,
    '환영':255,
    '자바':231,
    '장고':175,
    '자바스크립트':152,
    '스프링':109,
    '부트':71,
    '스타벅스':68,
    '제주말차':59,
    '프라푸치노':21,
    '먹고싶다':19,
    '디저트':6,
    '꿀잼':2
}

wc = WordCloud(
    font_path = 'malgun.ttf', # 한글 글씨체 설정
    background_color='white', # 배경색은 흰색으로 
    colormap='Reds', # 글씨색은 빨간색으로
    mask=cand_mask, # 워드클라우드 모양 설정
).generate_from_frequencies(words)

# plt.figure(figsize=(5,5))
# plt.imshow(wc,interpolation='bilinear')
# plt.axis('off') 
# plt.show()


txt='강아지 산책 강아지 목욕 강아지 미용 강아지 쇼핑 친구와 저녁 먹음 가족과 점심 먹음 혼자 저녁 먹음 친구와 쇼핑'
find_word = '강아지'

cnt = txt.count(find_word)
# print(cnt)

# plt.bar(find_word, cnt)
# plt.ylim(0, 10)
# plt.show()

# 문서를 갖고 와서 토큰화(형태소분석)하면 아래와 같은 자료가 생성됨
# tf-idf나 연관도 분석을 하려면 행을 합치면 안됨
txtList=['강아지 산책 강아지 목욕 강아지 미용 강아지 쇼핑',
'친구와 저녁 먹음 가족과 점심 먹음 혼자 저녁 먹음 친구와 쇼핑']
find_word='강아지'

# 워드클라우드 하려면
# txtList = txtList[0] + txtList[1]
txtList = ''.join(txtList)
cnt = txtList.count(find_word)
print(cnt)

# 일정한 단어만 count하고자 할때
f_word = ['강아지', '파이썬', '친구']

cnt = []
for i in f_word:
    cnt.append(txt.count(i))
percent = (np.array(cnt)/sum(cnt))*100
# print(percent)