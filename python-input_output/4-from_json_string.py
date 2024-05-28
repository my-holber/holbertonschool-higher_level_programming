#!/usr/bin/python3
"""Module that contains a function that returns an object represented by a JSON string"""
import json

def from_json_string(my_str):
    """Function that returns an object represented by a JSON string

    Args:
        my_str: JSON string

    Raises:
        Exception: if the JSON string cannot be decoded

    """
    return json.loads(my_str)
