import requests
from bs4 import BeautifulSoup
header = {'user-agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
URl = 'https://scitechdaily.com/news/technology/'
def article_update():
    web = requests.get(URl, headers=header)
    soup = BeautifulSoup(web.content, 'lxml')
    articles = soup.find_all('article', class_='content-list')
    for article in articles:
        article_heading = article.find('h3', class_='entry-title').get_text()
        article_info = article.find('div', class_='content-list-excerpt').get_text()
        article_link = article.header.h3.a['href']
        print(f'Heading: {article_heading.strip()}')
        print(f'Small detail: {article_info.strip()}')
        print(f'Link to this article: {article_link}')
        print("")

article_update()
