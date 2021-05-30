import requests
from bs4 import BeautifulSoup
website = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
print('type a skill you are unfamiliar with')
unfamiliar_skill = input('> ')
print(f'filtering out {unfamiliar_skill}')
soup = BeautifulSoup(website.content, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    availability = job.find('span', class_='sim-posted').span.text
    if 'few' in availability:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", '')
        skills = job.find('span', class_='srp-skills').text.replace(" ", '')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f'company name: {company_name.strip()}')
            print(f'skills: {skills.strip()}')
            print(f'More info: {more_info.strip()}')
            print("")


'''
import requests
from bs4 import BeautifulSoup
header = {'user-agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
URL = 'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5VSQNG/ref=sr_1_1_sspa?dchild=1&keywords=macbook&qid=1622280349&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTjkxQ0Y3Nk04Wk5EJmVuY3J5cHRlZElkPUEwMzcxMzc5MVY5RDBaQVVXOFZIUCZlbmNyeXB0ZWRBZElkPUEwNTA4NzY5NzYxUENGT1gyTDYxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
def check_price():
    html = requests.get(URL, headers=header)
    soup = BeautifulSoup(html.content, 'lxml')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    converted_price = price.replace(',', '')
    converted_price = converted_price[1:8]
'''