from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('p','title')
#CHARTrealtime > table > tbody > tr:nth-child(2) > th > p > a
#results = soup.select('CHARTrealtime > table > tbody > tr:nth-child(2) > th > p > a')

search_rank_file = open("practice1.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1