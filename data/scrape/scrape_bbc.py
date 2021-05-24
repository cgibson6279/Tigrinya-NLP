#!/usr/bin/env python
"""Scrapes https://www.dendenmedia.com/ Tigrinya website for text data."""

import argparse
import requests 
from requests import get

from bs4 import BeautifulSoup
import re
import unicodedataplus

def main(args: argparse.Namespace):
    URL = args.URL
    BBC_PATH = "data/BBC"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get links to articles.
    article_list = soup.find_all("h3")
    link_list = [] 
    for article in article_list:
        link = article.find("a")['href']
        if "http" not in link:
            link_list.append(link)
    for link in link_list:
        with open(BBC_PATH + "/" + link.split("/")[2], "w", encoding="UTF-8") as out_path:
            url = "https://www.bbc.com" + link 
            news = requests.get(url)
            news_soup = BeautifulSoup(news.content,'html.parser')
            paragraphs = news_soup.find_all("p")
            for p in paragraphs: 
                string = p.text
                text = ""
                for char in string: 
                    if unicodedataplus.script(char) == "Ethiopic" or char == " " or char.isnumeric():
                        text += char
                if not text.isspace():
                    if text != "":
                        print(text, file=out_path)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("URL", help="URL to https://www.dendenmedia.com.")
    main(parser.parse_args())