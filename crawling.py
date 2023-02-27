import requests
from bs4 import BeautifulSoup

url = 'https://www.mk.co.kr/'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # container > section > div.mk_head_news_group > div > div > div.col.sub_col > section.news_sec.top_news_sec.is_active > div > div > ul > li:nth-child(1) > a
    # container > section > div.mk_head_news_group > div > div > div.col.sub_col > section.news_sec.top_news_sec.is_active > div > div > ul > li:nth-child(2) > a
    links = soup.select('#container .top_news_list > li > a')
    cell_line = []
    for i in links:
        href = i.attrs['href']
        cell_line.append(href)
    print(cell_line)
else :
    print(response.status_code)

for i in cell_line:
    html = requests.get(i).text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#container h2').get_text()
    print(title)