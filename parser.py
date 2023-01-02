
import requests
from bs4 import BeautifulSoup as bs

page = requests.get(
  "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%99%98%EC%9C%A8"
)

soup = bs(page.text, "html.parser")  #응답받은 html내용을 객체형태로 생성

#print(soup)

# elements = soup.select('table.rate_table_info tbody tr.dw td > span')
"""
code = soup.select(
 'table,rate_table_info tbody tr.dw th:nth-of-type(1) a'
)
"""
"""
codeUp= soup.select(
    'table.rate_table_info tbody tr.up th a'
)

exchangeratesUp = soup.select(
    'table.rate_table_info tbody tr.up th span'
)

codeDw = soup.select(
    'table.rate_table_info tbody tr.dw th a'
)
exchangeratesDw = soup.select(
  'table.rate_table_info tbody tr.dw td:nth-of-type(1) span'
)

for index, element in enumerate(codeUp, 1):
    print(element.text)


for index, element in enumerate(exchangeratesUp, 1):
    print(element.text)

for index, element in enumerate(codeDw, 1):
    print(element.text)


for index, element in enumerate(exchangeratesDw, 1):
    print(element.text)

#for index, element in enumerate(exchangerates, 1):
 # print(element.text)

"""
currency_code = soup.select(
    'div.rate_table_bx._table > table > tbody > tr > th > a'
)

currency_rate = soup.select(
    'div.rate_table_bx._table > table > tbody > tr > td:nth-child(2) > span'
)

for index, element in enumerate(currency_code, 1):
    print(element.text)


for index, element in enumerate(currency_rate, 1):
    print(element.text)
