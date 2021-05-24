#!/usr/bin/env python
"""Split data into test, train, validate sets."""

import argparse
import random


def main(args: argparse.Namespace) -> None:
    with open(args.file, "r") as src:
        lines = []
        for line in src:
            lines.append(line.rstrip())
        # Set test, train and train sample sizes.
        train_sample = int(len(lines) * 0.8)
        test_sample = int(len(lines) * 0.1)
        # Shuffle data for sampling
        random.Random(42).shuffle(lines)
        # Split data into test, train,split
        train = lines[0:train_sample]
        valid = lines[train_sample : train_sample + test_sample]
        test = lines[train_sample + test_sample :]
        # Create train file.
        with open("data/train_data/tok.train", "w") as out_path:
            for line in train:
                print(line, file=out_path)
        # Create validation file.
        with open("data/train_data/tok.valid", "w") as out_path:
            for line in valid:
                print(line, file=out_path)
        # Create test file.
        with open("data/train_data/tok.test", "w") as out_path:
            for line in test:
                print(line, file=out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Path to tokenized data for splitting.")
    main(parser.parse_args())
