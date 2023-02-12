import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/news/news_list.naver?mode=RANK'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    #contentarea_left > div.hotNewsList > ul > li:nth-child(1)
    links = soup.select('#contentarea_left > div.hotNewsList > ul > li > ul > li > a')
    cell_line = []
    for i in links:
        href = i.attrs['href']
        cell_line.append(href)
        print(cell_line)
else :
    print(response.status_code)


#기업, 종목분석
#https://finance.naver.com/news/news_list.naver?mode=LSS3D&section_id=101&section_id2=258&section_id3=402


#contentarea_left > ul > li.newsList.top > dl > dd:nth-child(2)
#contentarea_left > ul > li.newsList.top > dl > dd:nth-child(5)
#contentarea_left > ul > li.newsList.top > dl > dd:nth-child(11)