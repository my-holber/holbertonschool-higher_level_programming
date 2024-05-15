#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        _dict = max(a_dictionary)
        if not _dict:
            return None
        return _dict
