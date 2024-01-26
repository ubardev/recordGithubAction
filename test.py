import requests
from bs4 import BeautifulSoup

url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.list_title')
for no, book in enumerate(bookservices, 1):
  print(no, book.text.strip())
