#!/usr/bin/env python
"""Evaluate tokenizer."""
import argparse
import logging

from tig_tokenizer import TigrinyaTokenizer


def main(args: argparse.Namespace) -> None:
    tokens = 0
    correct_tokens = 0
    sentences = 0
    correct_sentences = 0
    with open(args.gold, "r") as gold, open(args.hpyo, "r") as hypo:
        for (lineno, (gold_line, hypo_line)) in enumerate(zip(gold, hypo), 1):
            gold_tokens = gold_line.split()
            hypo_tokens = TigrinyaTokenizer().tokenize(hypo_line)
            if len(gold_tokens) != len(hypo_tokens):
                pass
                logging.error("Length mismatch at line %d", lineno)
                print(f"gold:{gold_tokens}\ntokenized:{hypo_tokens}")
            correct_sentence = True
            for (gold_token, hypo_token) in zip(gold_tokens, hypo_tokens):
                if gold_token == hypo_token:
                    correct_tokens += 1
                else:
                    correct_sentence = False
                tokens += 1
            correct_sentences += correct_sentence
            sentences += 1
    print(f"Word accuracy:\t\t{100 * correct_tokens / tokens:.2f}%")
    print(f"Sentence accuracy:\t{100 * correct_sentences / sentences:.2f}%")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gold", help="Path to gold tokenized file.")
    parser.add_argument("hpyo", help="Path to file for tokenization.")
    main(parser.parse_args())
