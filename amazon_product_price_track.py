import requests
from bs4 import BeautifulSoup
import smtplib
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
    if converted_price < '100000':
        sendmail()

def sendmail():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login("pythonteseting@gmail.com", 'FuckGmail@99')
    subject = 'Amazon product'
    body = f'check the amazon link ' \
           f'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5VSQNG/ref=sr' \
           f'_1_1_sspa?dchild=1&keywords=macbook&qid=1622280349&sr=8-1-spons&psc=1&spLa=' \
           f'ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTjkxQ0Y3Nk04Wk5EJmVuY3J5cHRlZElkPUEwMzcxMzc5MVY5RDBaQVVXOFZI' \
           f'UCZlbmNyeXB0ZWRBZElkPUEwNTA4NzY5NzYxUENGT1gyTDYxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZ' \
           f'WN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== ' \
           f'price has dropped'

    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(
         'pythonteseting@gmail.com',
         'aqeelsayadat007@gmail.com',
         msg
    )
    print('E-mail has been sent')
    server.quit()

check_price()