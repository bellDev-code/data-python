from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil

try:
    shutil.rmtree(r"c:\chrometemp")
except FileNotFoundError:
    pass

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


def get_page_count(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find('nav', class_="ecydgvn0")
    
    if pagination == None:
        return 1
    pages = pagination.find('div', recursive=False)
    print(len(pages))
    
get_page_count("python")

def extract_indeed_jobs(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    browser.get(f"{base_url}{keyword}")

    results = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_='jobsearch-ResultsList')
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone == None:
            anchor = job.select_one("h2 a")
            title = anchor['aria-label']
            link = anchor['href']
            name = job.find("span", class_= "companyName")
            location = job.find("div", class_="companyLocation")
            job_data = {
                'link': f"https://kr.indeed.com{link}",
                'company': name.string,
                'location': location.string,
                'position': title,
            }
            results.append(job_data)      
    for result in results:
        print(result, "/////\n///////")
        
        
extract_indeed_jobs("python")