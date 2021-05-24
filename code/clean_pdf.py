#!/usr/bin/env python

"""Get Tigrinya text from voice translations."""

import argparse
import os

import unicodedata


def main(args: argparse.Namespace) -> None:
    PUNCTUATION = ["comma", "space", "exclamation mark", "hyphen-minus"]
    for file in os.listdir(args.eval):
        if file.endswith(".tok"):
            with open(f"{args.eval}/{file}", "r", encoding="UTF-8") as src:
                with open(
                    f"{args.eval}/eval.tok", "w", encoding="UTF-8"
                ) as out:
                    for line in src:
                        tig_sent = ""
                        line_check = []
                        for char in line:
                            try:
                                if (
                                    "ethiopic"
                                    in unicodedata.name(char).lower()
                                ):
                                    tig_sent += char
                                    line_check.append(
                                        unicodedata.name(char).lower()
                                    )
                                if (
                                    unicodedata.name(char).lower()
                                    in PUNCTUATION
                                ):
                                    tig_sent += char
                                    line_check.append(
                                        unicodedata.name(char).lower()
                                    )
                            except ValueError:
                                pass
                        line_check = " ".join(line_check)
                        if "ethiopic" in line_check:
                            print(tig_sent, file=out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eval", help="Path to evaluation data for cleaning.")
    main(parser.parse_args())
