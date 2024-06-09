try:
    from newsapi import NewsApiClient
except ModuleNotFoundError as e:
    print("Try `pip install newsapi-python`")

# Init
NEWSAPI = NewsApiClient(api_key='30dd97580b75404d87cd28ec1a2b0a6d') # My API Key
URLS_EXCLUDED = ["https://removed.com"]

def get_top_headlnes():

    global NEWSAPI

    # get top-headlines
    top_headlines = NEWSAPI.get_top_headlines(q='flu',
                                            language='en')

    urls = [article["url"] for article in top_headlines['articles']]

    return urls # TODO: Come up with a way to consume this url using scrapers, etc.
