import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#wrap-body > #body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    a_tag = song.select_one('td.info > a')
    if a_tag is not None:
        rank = ((song.select_one('td.number')).text).split()[0]
        title = a_tag.text 
        singer =  (song.select_one('td.info > a.artist.ellipsis')).text
        title_only = title.strip()  
        singer_only = singer.strip() 
        print(rank, title_only, singer_only)