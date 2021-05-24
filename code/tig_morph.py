#!/usr/bin/env python
"""Implement HornMorph functions for morphological
analysis, segmentation and phonological transcriptions."""

import hm
from typing import Dict, List


def _analyze(lang, token: str) -> List[Dict]:
    """Get morphological analysis from HornMorpho.
    A list of Python dicts is returned, one for each
    analysis, with keys for lemma, gloss, and grammatical
    features ('gram').
    
    The grammatical features returned are in the form
    of a feature structure, a kind of dict with grammatical
    feature names as keys and their values as values.
    Among the features you may find useful are
    sb (subject), tm (tense-aspect-modality), ob (object).
    (A complete description of these features will appear soon.)
    """
    return hm.anal("ti", token=token, um=True)


def _segment(token: str) -> List[List[str]]:
    """The function hm.seg takes a language abbreviation and a
    word in conventional orthography and returns a segmentation
    of the word. Morphemes are separated by hyphens, with an
    indication of the grammatical features associated with each
    morpheme following it in parentheses. For Amharic verbs,
    the stem appears in curly brackets. Within the stem the root
    and the consonant-vowel template are separated by a plus sign.
    """
    return hm.seg("ti", token=token, realize=True)


def _phon(token: str) -> List[str]:
    """ The function hm.phon takes a string abbreviation of a language
    and an orthographic representation of a word and prints out a
    romanized representation of the pronunciation of the word, including
    gemination and epenthesis, where appropriate. Note that there may be
    multiple possible pronunciations.
    """
    return hm.phon("ti", token=token, raw=True).split()
