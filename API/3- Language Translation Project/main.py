from newsapi import NewsApiClient

# Instantiate the NewsApiClient object using your API key
api = NewsApiClient(api_key='your_api_key')

# Retrieve the top headlines
top_headlines = api.get_top_headlines()

# Print the titles and descriptions of the articles
for article in top_headlines['articles']:
    print('Title:', article['title'])
    print('Description:', article['description'])
    print()



"""
Make sure to replace your_api_key with your actual API key. From > https://newsapi.org/ <
"""