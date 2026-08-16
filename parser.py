import requests
from bs4 import BeautifulSoup


def parse_habr_top_daily_articles(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    articles = soup.find_all(class_="tm-articles-list__item")

    for i, article in enumerate(articles, 1):
        title = article.find(class_="tm-title__link").text
        views = article.find(class_="tm-icon-counter__value").text

        print(f"{i}. {title} | Просмотры: {views}")

