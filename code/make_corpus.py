#!/usr/bin/env python
"""Create sent text corpus of from Haddas Ertra"""

import os

from nltk import word_tokenize
import re
from unicodedata import *
import unicodedataplus
from typing import List

HADDAS_ERTRA_PATH = "data/haddas_ertra"
BBC_PATH = "data/BBC"


def main():
    with open("data" + "/" + "hp.tok", "w", encoding="UTF-8") as out_path:
        for file in os.listdir(HADDAS_ERTRA_PATH):
            try:
                with open(
                    HADDAS_ERTRA_PATH + "/" + file, "r", encoding="UTF-8"
                ) as article:
                    for line in article:
                        line = line.rstrip()
                        line = line.replace("2019", "")
                        if line != "":
                            print(line, file=out_path)
            except UnicodeDecodeError:
                pass
        for file in os.listdir(BBC_PATH):
            with open(BBC_PATH + "/" + file, "r", encoding="UTF-8") as article:
                for line in article:
                    line = line.rstrip()
                    print(line.rstrip(), file=out_path)


if __name__ == "__main__":
    main()
