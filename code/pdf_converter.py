#!/usr/bin/env python

"""Convert PDFs to .txt files."""
import argparse
import os

import txt_processing as tp


def main(args: argparse.Namespace) -> None:
    # Run through files in a directory
    for file in os.listdir(args.PDF):
        if file.endswith(".pdf"):
            file_name = file.split(".")[0]
            text = tp.convert_pdf_to_string(f"{args.PDF}/{file}")
            with open(f"{args.txt}/{file_name}.tok", "w") as txt_file:
                print(
                    text.encode("utf-8").decode("utf-8").rstrip(),
                    file=txt_file,
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("PDF", help="Path to PDF directory for conversion.")
    parser.add_argument("txt", help="Path to text directory to write file.")
    main(parser.parse_args())
