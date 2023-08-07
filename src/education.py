import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

file_name = 'd:/data/education.csv'

# gender: 학생의 성별 (M: 남성, F: 여성)
# NationaliTy: 학생의 국적
# PlaceofBirth: 학생이 태어난 국가
# StageID: 학생이 다니는 학교 (초,중,고)
# GradeID: 학생이 속한 성적 등급
# SectionID: 학생이 속한 반 이름
# Topic: 수강한 과목
# Semester: 수강한 학기 (1학기/2학기)
# Relation: 주 보호자와 학생의 관계
# raisedhands: 학생이 수업 중 손을 든 횟수
# VisITedResources: 학생이 과목 공지를 확인한 횟수
# Discussion: 학생이 토론 그룹에 참여한 횟수
# ParentAnsweringSurvey: 부모가 학교 설문에 참여했는지 여부
# ParentschoolSatisfaction: 부모가 학교에 만족했는지 여부
# StudentAbscenceDays: 학생의 결석 횟수 (7회 이상/미만)
# Class: 학생의 성적 등급 (L: 낮음, M: 보통, H: 높음)

edu = pd.read_csv(file_name, sep=",")

# print(edu.info())
# edu.describe()

gender_cnt = edu['gender'].value_counts()

national_cnt = edu['NationalITy'].value_counts()

birth_cnt = edu['PlaceofBirth'].value_counts()

class_cnt = edu['Class'].value_counts()
total_L_count = class_cnt['L']
# print(total_L_count)

class_ = ['L', 'M', 'H']

# seaborn의 hitplot, joinplot, pairplot 히스토그램
# kde 커널밀도추정
# 학생이 수업 중 손을 든 횟수에 따른 학생의 성적 등급간의 관계를 알 수 있다.
# sns.histplot(x='raisedhands', data=edu, hue='Class', hue_order=class_, kde=True)
# plt.show()
# 학생이 과목 공지를 확인한 횟수에 따른 학생의 성적 등급간의 관계
# sns.histplot(x='VisITedResources', data=edu, hue='Class', hue_order=class_, kde=True)
# plt.show()

# 즉, 수업 중 손을 든 횟수에 따른학생의 성적, 과목 공지를 확인한 횟수에 따라 성적 등급간의 관계를 알 수 있다.
# 손을 든 횟수가 낮고, 과목 공지를 확인하지 않은 학생의 등급은 L등급이 많다.
# sns.jointplot(x='VisITedResources', y='raisedhands', data=edu, hue='Class', hue_order=class_)

# jointplot? 산점도를 기본으로 표시하고 x-y축에 각 변수에 대한 히스토그램을 동시에 보여준다.
# 두 변수의 관계와 데이터가 분산되어 있는 정도를 한눈에 파악할 수 있다.
# plt.show()

# 학생이 공지사항을 확인한 횟수에 따른 학생의 성적 등급간의 관계
# sns.histplot(x='AnnouncementsView', data=edu, hue='Class', hue_order=class_, kde=True)
# plt.show()

# 학생이 토론을 하는 횟수에 따른 학생의 성적 등급간의 관계
# sns.histplot(x='Discussion', data=edu, hue='Class', hue_order=class_, kde=True)
# plt.show()

# pairplot : 인자로 전달되는 데이터프레임의 열(변수)을 두 개씩 짝 지을 수 있는 모든 조합에 대해서 표현
# 열은 int형이여야 한다.
# sns.pairplot(edu, hue='Class', hue_order=['L', 'M', 'H'])
# plt.show()

# countplot을 활용한 점수 총합
# sns.countplot(x='Class', data=edu, order=class_)
# plt.show()

# 성별에 따른 점수 분포수
# sns.countplot(x='gender', data=edu, hue='Class', hue_order=['L', 'M', 'H'])
# plt.show()

# sns.countplot(x='NationalITy', data=edu, hue='Class', hue_order=class_)
# plt.xticks(rotation=90)
# plt.show()

# 부모가 설문조사에 참여함에 따른 학생의 점수 수
# sns.countplot(x='ParentAnsweringSurvey', data=edu, hue='Class', hue_order=class_)
# plt.show()

# sns.countplot(x='ParentschoolSatisfaction', data=edu, hue='Class', hue_order=class_)
# plt.show()

edu['Class_value'] = edu['Class'].map(dict(L=-1, M=0, H=1))
# Class_value 열의 평균 계산
gb = edu.groupby('gender')['Class_value'].mean()
# plt.bar(gb.index, gb)
# plt.show()

tb = edu.groupby('Topic')['Class_value'].mean().sort_values()
# plt.barh(tb.index, tb)
# plt.show()

sb = edu.groupby('StudentAbsenceDays')['Class_value'].mean().sort_values(ascending=False)
# plt.barh(sb.index, sb)
# plt.show()


# 머신러닝 예측분석이 필요한 경우만 작업

# print(edu.info())
# get_dummies()를 이용하여 범주형 데이터 전처리 하기
X = pd.get_dummies(edu.drop(['ParentschoolSatisfaction', 'Class', 'Class_value'], axis=1),
                   columns=['gender', 'NationalITy', 'PlaceofBirth',
                            'StageID', 'GradeID','SectionID', 'Topic',
                            'Semester', 'Relation', 'ParentAnsweringSurvey',
                            'StudentAbsenceDays'],
                   drop_first=True)
y = edu['Class']

# 학습 데이터와 테스트 데이터 분리하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Classification 모델 학습하기
# Logistic Regression 모델
model_lr = LogisticRegression(max_iter=10000)
model_lr.fit(X_train, y_train)

pred = model_lr.predict(X_test)
print(classification_report(y_test, pred))