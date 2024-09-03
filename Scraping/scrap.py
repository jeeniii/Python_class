import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
data = requests.get('https://www.melon.com/chart/index.htm', headers=headers) # 멜론 차트
soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')

# 50 이후에 100을 출력
top_50 = soup.select('#lst50 > td > div')
top_100 = soup.select('#lst100 > td > div')

# for tr50 in top_50:
#     rank = tr50.select_one('span.rank')

#     if rank is not None:
#         print(rank.text, end=" ")
    
#     title = tr50.select_one('div > div.ellipsis.rank01 > span > a')

#     if title is not None:
#         print(title.text)

# for tr100 in top_100:
#     rank = tr100.select_one('span.rank')

#     if rank is not None:
#         print(rank.text, end=" ")
    
#     title = tr100.select_one('div > div.ellipsis.rank01 > span > a')

#     if title is not None:
#         print(title.text)

# 50과 100을 합쳐서 반복문 실행
all_top = top_50 + top_100

for trAll in all_top:
    rank = trAll.select_one('span.rank')

    if rank is not None:
        print(rank.text, end=" - ")

    title = trAll.select_one('div > div.ellipsis.rank01 > span > a')

    if title is not None:
        print(title.text)