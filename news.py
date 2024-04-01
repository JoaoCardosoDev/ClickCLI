import click
import requests
from datetime import datetime
from send_email import *

current = datetime.now()
parsedCurrent = current.strftime("%d/%m/%Y, %H:%M")

@click.command()
@click.option('--choice', prompt=f'Welcome, today is {parsedCurrent}, would you like to read the news or order breakfast?\n[news | breakfast]', help='Valid answers are: news | breakfast')
def welcome(choice):
    """
    Welcomes the user gives choice for news or ordering breakfast.
    """
    if choice == "breakfast":
        change_body()
    elif choice == "news":
       news()
    else:
        click.echo("Invalid input.")



@click.command()
@click.option('--choice', prompt='Would you like to search for news by topic or country?\n[topic | country]', help='Valid answers are: topic | country')
def news(choice):
    """
    Lets the user choose the scope of news to peruse.
    """
    if choice == "topic":
        topic()
    elif choice == "country":
        country()
    else:
        click.echo("Invalid input. Use [news welcome -h] for more information.")


@click.command()
@click.option('--country', prompt=("Use the ISO country code to search for the headlines of your choosing:\n['pt'|'us'|etc]: "), help='Input ISO code of country to return headlines.')
@click.option('--entries', prompt=("How many entries would you like to have?\n[Number of entries]: "), type=int, help='Input the number of entries you would like to view on screen.' )
def country(country, entries):
    """
    Let's the user choose the country they would like to see news from and aditionally prompts for the number of entries.
    """
    url = f"https://newsapi.org/v2/top-headlines?country="+country+"&apiKey=24ff6827b3d0431b8a1ac316bdfa5f31"
    response = requests.get(url)
    response = response.json()
    articles = response.get("articles", [])
    print("-" * 50 + "News!" + "-" * 50)
    display(articles, entries)


@click.command()
@click.option('--search', prompt=("Search topics by: title, description, content or category.\n[Search]: "), help='Input the search parameter.', type=str)
@click.option('--entries', prompt=("How many entries would you like to have?\n[Number of entries]: "), type=int, help='Input the number of entries you would like to view on screen.' )
def topic(search, entries):
    """
    Let's the user choose the topic they would like to see news from and aditionally prompts for the number of entries.
    """
    url = "https://newsapi.org/v2/everything?q=" + search + "&apiKey=24ff6827b3d0431b8a1ac316bdfa5f31"

    response = requests.get(url)
    response = response.json()
    articles = response.get("articles", [])
    print("-" * 50 + "News!" + "-" * 50)
    display(articles, entries)



def display(articles, entries):
       counter = 0

       for article in articles:
              title = article.get("title")
              if title == "[Removed]":
                     continue
              print("Title:", title)
              print("Author:", article.get("author"))
              if article.get("description") != None:
                     print("Description:", article.get("description"))
              if article.get("content") != None:
                     print("Content:", article.get("content"))
              print("URL:", article.get("url"))
              print("-" * 106)
              counter += 1
              if counter >= entries:
                     break
    
if __name__ == '__main__':
    welcome()