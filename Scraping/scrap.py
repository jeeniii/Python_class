import requests
from bs4 import BeautifulSoup

# req = requests.get('https://www.melon.com/chart/') #url 입력

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
data = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
top_100 = soup.select('#lst50 > td > div')

for tr in top_100:
    # rank = tr.select_one('span.rank')

    # if rank is not None:
    #     print(rank.text, end=" ")
    
    title = tr.select_one('div > div.ellipsis.rank01 > span > a')

    if title is not None:
        print(title.text)

