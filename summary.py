from gensim.summarization.summarizer import summarize
from newspaper import Article

url ='https://n.news.naver.com/mnews/article/014/0004967918?sid=101'
news = Article(url)
news.download()
news.parse()
text = summarize(news.text, ratio=0.4)
print("=====")
print(text)
print("=====")