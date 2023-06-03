#print titles and description of articles
import json
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='31e18fbb16774e52a6558b51aff5f819_suhail')
top_headlines=newsapi.get_top_headlines()
print()
for i in range(len(top_headlines["articles"])):
    dict1=top_headlines["articles"][i]
    print(f"Title: {dict1['title']}")
    print(f"Description: {dict1['description']}")
    print()