#!/usr/bin/env python
"""Scrapes https://www.dendenmedia.com/ Tigrinya website for text data."""

import argparse
from requests import get

from bs4 import BeautifulSoup
import re
import unicodedataplus

def main(args: argparse.Namespace):
    URL = args.URL
    HADDAS_ERTRA_PATH = "data/haddas_ertra" 
    while True:
        try:
            REGEX = re.compile('(\d+[-/]\d+[-/]\d+)')
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            date = re.search(REGEX,URL).group(0).replace("/","-")
            print(date)
            # Get article title.
            title = soup.find("h1", class_="entry-title").text.rstrip()
            with open(HADDAS_ERTRA_PATH + "/" + date, "w", encoding="UTF-8") as out_path:
                print(title,file=out_path)
                print("",file=out_path)
                paragraphs = soup.find_all("p")
                for p in paragraphs:
                    string = p.text
                    text = ""
                    for char in string: 
                        if unicodedataplus.script(char) == "Ethiopic" or char == " " or char.isnumeric():
                            text += char
                    if not text.isspace():
                        if text != "":
                            print(text, file=out_path)
            link = soup.find("div", class_="vlog-next-link")
            next_link = link.find("a")['href']
            URL = next_link
        except AttributeError:
            break


if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("URL", help="URL to https://www.dendenmedia.com.")
    main(parser.parse_args())