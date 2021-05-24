#!/usr/bin/env python
"""Word tokenize text."""

import re
from nltk.tokenize.api import TokenizerI
from nltk.tokenize.util import align_tokens


class TigrinyaTokenizer(TokenizerI):
    # Starting quotes
    STARTING_QUOTES = [
        (re.compile(r"^\""), r"``"),
        (re.compile(r"(``)"), r" \1 "),
        (re.compile(r"([ \(\[{<])(\"|\'{2})"), r"\1 `` "),
    ]
    # Punctuation + Tigrinya punctuation
    PUNCTUATION = [
        # Match :, and a single non-digit character.
        (re.compile(r"([:,])([^\d])"), r" \1 \2"),
        # Match :, at the end of a string.
        (re.compile(r"([:,])$"), r" \1 "),
        # Match elipses.
        (re.compile(r"\.\.\."), r" ... "),
        # Adds spaces before and after group item 0.
        (re.compile(r"[;@#$%&]"), r" \g<0> "),
        (
            # Adds space between word final period,
            # quotation, etc. combination and
            # preceding word
            re.compile(r'([^\.])(\.)([\]\)}>ß"\']*)\s*$'),
            r"\1 \2\3 ",
        ),  # Handles the final period.
        (re.compile(r"[?!¡]"), r" \g<0> "),
        (re.compile(r"([^'])' "), r"\1 ' "),
        # Add space before and after Tigrinya punctuation
        (re.compile(r"[።፣፤፥፦፧፨፠፡]"), r" \g<0> "),
    ]
    # Pads parentheses
    PARENS_BRACKETS = (re.compile(r"[\]\[\(\)\{\}\<\>]"), r" \g<0> ")
    # Optionally: Convert parentheses,
    # brackets and converts them to PTB symbols.
    CONVERT_PARENTHESES = [
        (re.compile(r"\("), "-LRB-"),
        (re.compile(r"\)"), "-RRB-"),
        (re.compile(r"\["), "-LSB-"),
        (re.compile(r"\]"), "-RSB-"),
        (re.compile(r"\{"), "-LCB-"),
        (re.compile(r"\}"), "-RCB-"),
    ]
    DOUBLE_DASHES = (re.compile(r"--"), r" -- ")
    # Ending quotes
    ENDING_QUOTES = [
        (re.compile(r'"'), " '' "),
        (re.compile(r"(\S)(\'\')"), r"\1 \2 "),
        (re.compile(r"([^' ])('[sS]|'[mM]|'[dD]|') "), r"\1 \2 "),
        (re.compile(r"([^' ])('ll|'LL|'re|'RE|'ve|'VE|n't|N'T) "), r"\1 \2 "),
    ]

    def tokenize(self, text, convert_parentheses=False, return_str=False):
        for regexp, substitution in self.STARTING_QUOTES:
            text = regexp.sub(substitution, text)
        for regexp, substitution in self.PUNCTUATION:
            text = regexp.sub(substitution, text)
        # Handles parentheses.
        regexp, substitution = self.PARENS_BRACKETS
        text = regexp.sub(substitution, text)
        # Optionally convert parentheses.
        if convert_parentheses:
            for regexp, substitution in self.CONVERT_PARENTHESES:
                text = regexp.sub(substitution, text)
        # Handles double dash.
        regexp, substitution = self.DOUBLE_DASHES
        text = regexp.sub(substitution, text)
        # Add extra space to make things easier.
        text = " " + text + " "
        for regexp, substitution in self.ENDING_QUOTES:
            text = regexp.sub(substitution, text)
        return text if return_str else text.split()

    def span_tokenize(self, text):
        r"""
        Uses the post-hoc nltk.tokens.align_tokens to return the offset spans.

            >>> from nltk.tokenize import TreebankWordTokenizer
            >>> s = '''Good muffins cost $3.88\nin New (York).  Please (buy) me\ntwo of them.\n(Thanks).'''
            >>> expected = [(0, 4), (5, 12), (13, 17), (18, 19), (19, 23),
            ... (24, 26), (27, 30), (31, 32), (32, 36), (36, 37), (37, 38),
            ... (40, 46), (47, 48), (48, 51), (51, 52), (53, 55), (56, 59),
            ... (60, 62), (63, 68), (69, 70), (70, 76), (76, 77), (77, 78)]
            >>> list(TreebankWordTokenizer().span_tokenize(s)) == expected
            True
            >>> expected = ['Good', 'muffins', 'cost', '$', '3.88', 'in',
            ... 'New', '(', 'York', ')', '.', 'Please', '(', 'buy', ')',
            ... 'me', 'two', 'of', 'them.', '(', 'Thanks', ')', '.']
            >>> [s[start:end] for start, end in TreebankWordTokenizer().span_tokenize(s)] == expected
            True

            Additional example
            >>> from nltk.tokenize import TreebankWordTokenizer
            >>> s = '''I said, "I'd like to buy some ''good muffins" which cost $3.88\n each in New (York)."'''
            >>> expected = [(0, 1), (2, 6), (6, 7), (8, 9), (9, 10), (10, 12),
            ... (13, 17), (18, 20), (21, 24), (25, 29), (30, 32), (32, 36),
            ... (37, 44), (44, 45), (46, 51), (52, 56), (57, 58), (58, 62),
            ... (64, 68), (69, 71), (72, 75), (76, 77), (77, 81), (81, 82),
            ... (82, 83), (83, 84)]
            >>> list(TreebankWordTokenizer().span_tokenize(s)) == expected
            True
            >>> expected = ['I', 'said', ',', '"', 'I', "'d", 'like', 'to',
            ... 'buy', 'some', "''", "good", 'muffins', '"', 'which', 'cost',
            ... '$', '3.88', 'each', 'in', 'New', '(', 'York', ')', '.', '"']
            >>> [s[start:end] for start, end in TreebankWordTokenizer().span_tokenize(s)] == expected
            True

        """
        raw_tokens = self.tokenize(text)
        # Convert converted quotes back to original double quotes
        # Do this only if original text contains double quote(s) or double
        # single-quotes (because '' might be transformed to `` if it is
        # treated as starting quotes).
        if ('"' in text) or ("''" in text):
            # Find double quotes and converted quotes.
            matched = [m.group() for m in re.finditer(r"``|'{2}|\"", text)]

            # Replace converted quotes back to double quotes.
            tokens = [
                matched.pop(0) if tok in ['"', "``", "''"] else tok
                for tok in raw_tokens
            ]
        else:
            tokens = raw_tokens
        for tok in align_tokens(tokens, text):
            yield tok
