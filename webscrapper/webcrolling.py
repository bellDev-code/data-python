from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(), options=chrome_options)

base_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
search_term = '휴가'

browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source, "html.parser")
soup_ul = soup.find('ul', class_='list_news')
sop_div = soup_ul.find_all('div', class_="news_wrap api_ani_send")

news_list = []
for div in sop_div:
    info_txt=div.find('a', class_="info press").get_text()
    tit_txt=div.find("a", class_="news_tit").get_text()
    doc_txt=div.find('div', class_="news_dsc").get_text()
    news_list.append({"제목":tit_txt,
                     "내용":doc_txt,
                     "언론사":info_txt.replace('언론사 선정', "")})

news_df = pd.DataFrame(news_list)
print(news_df)
        