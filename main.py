import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from loguru import logger

URL = "https://habr.com/ru/articles/top/daily/"

ARTICLE_CLASS = "tm-articles-list__item"
TITLE_CLASS = "tm-title__link"
VIEWS_CLASS = "tm-icon-counter__value"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def fetch_content(url: str) -> str | None:
    try:
        response = requests.get(url, headers=headers, timeout=(3, 10))
        response.raise_for_status()
        return response.text
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")


def parse_articles(html: str):
    soup = BeautifulSoup(html, "lxml")
    articles_cards = soup.find_all(class_=ARTICLE_CLASS)

    articles = []
    for card in articles_cards:
        title = card.find(class_=TITLE_CLASS)
        views = card.find(class_=VIEWS_CLASS)

        if not title or not views:
            logger.warning("Пропущена статья без заголовка или статистики просмотров.")
            continue

        articles.append({
            "title": title.get_text(strip=True),
            "views": views.get_text(strip=True)
        })

    return articles


def print_articles(articles: list[dict]):
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']} | Просмотры: {article['views']}")


def main():
    html = fetch_content(URL)
    articles = parse_articles(html)
    print_articles(articles)


if __name__ == "__main__":
    main()