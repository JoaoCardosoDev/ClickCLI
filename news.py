import click
import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-03-26&'
       'sortBy=popularity&'
       'apiKey=24ff6827b3d0431b8a1ac316bdfa5f31')

response = requests.get(url)

print (r.json)
