import requests
import time
from bs4 import BeautifulSoup

PTT_URL = 'https://www.ptt.cc'

def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html5lib')

    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []
    divs = soup.find_all('div', 'r-ent')
    name = soup.find('a','board').text
    for d in divs:
        if d.find('div', 'date').text.strip() == date:
            if d.find('a'):
                href = d.find('a')['href']
                title = d.find('a').text
                author = d.find('div', 'author').text if d.find('div', 'author') else ''
                articles.append({
                    'name': name,
                    'date': date,
                    'title': title,
                    'link': href,
                    'author': author
                })
    return articles, prev_url


def get_author_ids(posts, pattern):
    ids = set()
    for post in posts:
        if pattern in post['author']:
            ids.add(post['author'])
    return ids

if __name__ == '__main__':
    current_page = get_web_page(PTT_URL + '/bbs/Gossiping/index.html')
    if current_page:
        articles = []
        today = time.strftime("%m/%d").lstrip('0')
        current_articles, prev_url = get_articles(current_page, today)
        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)
        for a in articles:
                print(a['name'])
                print('日期：%s' % a['date'])
                print('作者：%s' % a['author'])
                print('標題：%s' % a['title'])
                print('連結：',PTT_URL+a['link'])
                print('---------------')
