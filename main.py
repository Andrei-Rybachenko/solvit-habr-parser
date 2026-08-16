from parser import parse_habr_top_daily_articles

URL = "https://habr.com/ru/articles/top/daily/"


if __name__ == "__main__":
    parse_habr_top_daily_articles(URL)