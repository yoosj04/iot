import requests
import bs4

response = requests.get("http://finance.naver.com/sise/")
html = bs4.BeautifulSoup(response.text, "lxml")
kospi = html.select_one('#KOSPI_now')
코스피 = kospi.text

print(" 오늘의 코스피 지수는 " + 코스피)