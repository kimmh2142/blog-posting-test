import requests
import schedule
import selenium.webdriver.common.devtools.v85.target
from selenium import webdriver
from bs4 import BeautifulSoup
from gensim.summarization.summarizer import summarize
from newspaper import Article
from datetime import datetime
import time


client_id = '26d963fd24fd21542a20987d515d3d4f'
client_secret = '26d963fd24fd21542a20987d515d3d4f370f69036d9e0a80025c6f70047d84bb41ce35c1'
access_token = '25316c0c8ed9b146238d706db37a886a_e514b92379bd7d84a8648a18215d0017'
code = '8bcf4b8a37494fd7f0587e7b677039e982fc3d222d2ddd76cbaaf3f90db2929f5c42c379'
redirect_uri = 'https://heeyaaaworld.tistory.com/'
blogName = 'heeyaaaworld'
tag = '오늘뉴스요약,뉴스요약'					#등록할 태그값, 쉼표로 구분
output = 'json'						#고정값
grant_type = 'authorization_code'   #고정값
visibility = 3  #0은 비공개, 3은 공개 발행
category = 617405

"""
def getToken():
    url = 'https://www.tistory.com/oauth/access_token?'
    data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'code': code,
            'grant_type': grant_type
            }
    r = requests.get(url, data)
    print (r.text)

def getCategory():
    url = 'https://www.tistory.com/apis/category/list?'
    data = {
            'access_token': access_token,
            'output': output,
            'blogName': blogName,
            }
    r = requests.get(url, data)
    print (r.text)
"""

def postWrite(content):
        #오늘 날짜 가져오기
        title = '['+datetime.today().strftime('%Y-%m-%d')+'] 오늘 아침 뉴스 요약'
        url = 'https://www.tistory.com/apis/post/write?'
        data = {
                 'access_token': access_token,
                 'output': output,
                 'blogName': blogName,
                 'title': title,
                 'content': content,
                 'visibility': visibility,
                 'category': category,
                 'tag': tag,
                 }
        r = requests.post(url, data=data)
        print ('자동 포스팅 성공')
        return r.text


if __name__ == '__main__':
    # getToken()    #최초 토큰 발급시에만 수행nn
    # getCategory()  #최초 카테고리 확인시에만 수행

    contents = ""
    driver = webdriver.Chrome("C://chromedriver.exe")
    driver.get("https://www.mk.co.kr/")
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 상위 뉴스기사 url 가져오기
    links = soup.select('#container .top_news_list > li > a')
    news_urls = []
    for i in links:
        href = i.attrs['href']
        news_urls.append(href)


    # 기사 안으로 들어가서 뉴스 내용 긁어오기
    for i in news_urls:
        url = driver.get(i)

        # N번째 기사 안으로 이동
        url

        # 제목 추출
        # response = requests.get(i)
        # if response.status_code == 200:
        html = requests.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#container h2').get_text()
        contents += '[##_Image|kage@bfFbIP/btr1lvZmULU/vKPvGCf3blOhbdGR8o8zO0/img.png|alignCenter|width="1284" height="705" data-origin-width="1284" data-origin-height="705" data-ke-mobilestyle="widthOrigin" filename="img.png" filemime="image/png"|||_##]'
        contents += '<br><br><b>'
        contents += title
        contents += "</b><br>"
        print(contents)
        time.sleep(2)
        # else:
        #    print(response.status_code)

        # 본문내용 요약
        news = Article(i)
        news.download()
        news.parse()

        text = summarize(news.text, ratio=0.2)
        contents += text
        contents += "<br><br><br><br>"
        print(contents)
        print("=====")
        time.sleep(2)

    postWrite(contents)


