#!/usr/bin/env python
"""Generate corpus vocabulary using HornMorph and log stats."""
import argparse
import logging

import json
import hm

from tig_tokenizer import TigrinyaTokenizer


def main(args: argparse.Namespace):
    corp_vocab = set()
    hm_vocab = set()
    multi_set = set()
    tig_hm_vocab = dict()
    with open(args.file, "r", encoding="UTF-8") as src:
        for line in src:
            tokenized_line = TigrinyaTokenizer().tokenize(line)
            for token in tokenized_line:
                # Get morphological analysis.
                corp_vocab.add(token)
                try:
                    analysis = hm.anal("ti", token, um=True)
                    if len(analysis) > 0:
                        hm_vocab.add(token)
                        tig_hm_vocab[token] = {}
                        # Because some token entries contain multiple
                        # morphological analyses, we create a dictionary
                        # entry for each analysis. Entries are produced
                        # based on the grammar.
                        for variant in analysis:
                            tig_hm_vocab[token][variant["gram"]] = {
                                # Add POS
                                "POS": variant["POS"],
                                # Add lemma
                                "lemma": variant["lemma"].split("|")[0],
                                # Add pronunciation
                                "pronunciation": variant["lemma"].split("|")[
                                    1
                                ],
                                # Add root
                                "root": variant["root"],
                                # Add gram
                                "gram": variant["gram"],
                            }
                    if len(analysis) >= 2:
                        multi_set.add(token)
                except (TypeError, ValueError, KeyError) as error:
                    pass
    # Write to hm.json.
    with open(args.json, "w") as outpath:
        json.dump(tig_hm_vocab, outpath, indent=4, ensure_ascii=False)
    # Get hm dataset coverage.
    logging.info(f"Corpus Vocab:\t\t{len(corp_vocab)}")
    logging.info(f"HornMorph Vocab:\t\t{len(hm_vocab)}")
    logging.info(
        f"Covered Corpus:\t\t{len(hm_vocab)}/{len(corp_vocab)}={100 * len(hm_vocab) / len(corp_vocab):.2f}%"
    )
    # Of the tokens in the corpus that are covered by HM,
    # how many are ambiguous?
    logging.info(
        f"Ambiguity Rate:\t\t{len(multi_set)}/{len(hm_vocab)}={100 * len(multi_set) / len(hm_vocab):.2f}%"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get line and token count for corpus."
    )
    parser.add_argument("file", help="Path to corpus file.")
    parser.add_argument("json", help="Path to corpus vocabulary json.")
    logging.basicConfig(
        filename="data/vocab.log", filemode="w", level=logging.DEBUG
    )
    main(parser.parse_args())
