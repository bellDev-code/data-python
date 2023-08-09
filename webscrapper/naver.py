import os
import sys
import urllib.request

import json 
import lxml
import requests
from bs4 import BeautifulSoup
import pandas as pd

client_id = "w03G8YdpHQdIGlfSlUmX" 
client_secret = "jqBvxWIYLd"

encText = urllib.parse.quote("태풍")

url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&start=1" # JSON 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    blog_data = json.loads(response_body)
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

result_list = []
for temp in blog_data['items']:
    temp_dict = {}
    link = temp['link']
    des = temp['description']

    if 'https://blog.' in link: # 모바일 형태로
        link = link.replace('https://blog.','https://m.blog.')
    temp_dict['link'] = link
    temp_dict['des'] = des
    result_list.append(temp_dict)

result_list

html = requests.get("https://m.blog.naver.com/ying61/223135944262")
soup = BeautifulSoup(html.text, "html.parser") # 해당 url의 html 소스코드를 가져옴
soup 

# 내용을 가져오려고 했을때 html 코드에서 class 값을 선택해서 가져와야 함
result = soup.select(".se-text-paragraph.se-text-paragraph-align-")
result_text = " "
for x in result:
    result_text += x.text

site = []
site_des = []

for link_temp in result_list:
    if 'https://m.blog.naver' in link_temp['link']:
        html = requests.get(link_temp['link'])
        soup = BeautifulSoup(html.text, "html.parser")
        result = soup.select(".se-text-paragraph.se-text-paragraph-align-")
        result_text = ""
        for temp in result:
            result_text += temp.text
        site.append(link_temp['link'])
        site_des.append(result_text)

# 위 값들을 데이터프레임으로 바꾸기

result_data = {}
result_data['site'] = site
result_data['site_des'] = site_des

df = pd.DataFrame(result_data)
df.head()

# df.to_csv("C:/Data/블로그 데이터.csv", encoding='utf-8-sig') # 파일로 저장하기