from gensim.summarization.summarizer import summarize
from newspaper import Article

url ='https://www.mk.co.kr/news/world/10659926'
news = Article(url)
news.download()
news.parse()
text = summarize(news.text, ratio=0.2)
print("=====")
print(text)
print("=====")