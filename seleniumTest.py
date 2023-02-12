import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from gensim.summarization.summarizer import summarize
from newspaper import Article
import time
#import pandas as pd

#def set_chrome_driver():
#    chrome_options = webdriver.ChromeOptions()
#    driver = webdriver.Chrome("C://chromedriver.exe", options=chrome_options)
#    return driver

#네이버 뉴스 > 부동산 켜기
driver = webdriver.Chrome("C://chromedriver.exe")
driver.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=260")
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#상위 뉴스기사 url 가져오기
links = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt.photo > a')
news_urls = []
for i in links:
    href = i.attrs['href']
    news_urls.append(href)
print(news_urls)

#기사 안으로 들어가서 뉴스 내용 긁어오기
for i in news_urls:
    url = driver.get(i)
    # 본문내용
    contents = ""

    #N번째 기사 안으로 이동
    url

    # 제목 추출
    #response = requests.get(i)
    #if response.status_code == 200:
    html = requests.get(i).text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#title_area > span').get_text()
    contents += title
    print(contents)
    time.sleep(1)
    #else:
    #    print(response.status_code)

    #본문내용 요약
    news = Article(i)
    news.download()
    news.parse()
    if news.text is not None:
        text = summarize(news.text, ratio=0.4)
        contents += text
        print(contents)
        print("=====")
        time.sleep(1)
    else:
        continue
#contentarea_left > div.hotNewsList > ul > li:nth-child(1)
#contentarea_left > div.hotNewsList > ul > li:nth-child(2)