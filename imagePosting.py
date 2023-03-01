import json
import requests

blogName = 'heeyaaaworld'
token = '25316c0c8ed9b146238d706db37a886a_e514b92379bd7d84a8648a18215d0017'
filepath = 'C:/todayNews.png'

files = {'uploadedfile': open(filepath, 'rb')}
params = {'access_token': token, 'blogName': blogName, 'targetUrl':blogName, 'output':'json'}
rd = requests.post('https://www.tistory.com/apis/post/attach', params=params, files=files)

try:
	item = json.loads(rd.text)
	print(json.dumps(item, indent=4))
	print("----------------------------------------------")
	print(item["tistory"]["replacer"])
	print(item["tistory"]["url"])
	print(item["tistory"]["status"])
except:
	print("Failed")