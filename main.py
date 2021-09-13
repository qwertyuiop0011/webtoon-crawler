import requests
from bs4 import BeautifulSoup

for k in range(1, 52):
    res = requests.get(f"https://comic.naver.com/webtoon/list?titleId=183559&weekday=mon&page={k}")

    soup = BeautifulSoup(res.text, "html.parser")

    title = str(soup.findAll('td', {'class': 'title'}))
    arr = title.split(">")

    for i in arr:
        try:
            if i.index("</a") > 0:
                print(i.split("<")[0])
        except ValueError:
            pass