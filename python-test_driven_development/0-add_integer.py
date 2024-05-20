#!/usr/bin/python3
"""Commentaire principal
qui décrit le fichier .py
fghjktyuio ghyjuiop ghjkl èuio , tyuio yuio yhjk  hjk
uiobn,okflgorg kevpkgeg
kerv ,kr,zfz,feàçgeigjegeoggr orgr   ei gj"""


def add_integer(a, b=98):
    """Adds two integers or floats,
        casted to integers first if they are float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(a, (int)):
        a = int(a)
    if not isinstance(b, (int)):
        b = int(a)
    return a + b
