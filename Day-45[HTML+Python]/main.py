from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_page_data = response.text

soup = BeautifulSoup(yc_page_data, "html parser")
soup.find("a")



