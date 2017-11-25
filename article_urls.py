import json, requests
from constants import NEWS_API_KEY

def find_articles_about(company):
    url = ("https://newsapi.org/v2/everything?q=" + company + "&apiKey=" + NEWS_API_KEY)
    response = requests.get(url)
    articles = json.loads(response.text)['articles']

    article_urls = list(map(lambda x: x["url"], articles))
    return article_urls

find_articles_about('Apple')
