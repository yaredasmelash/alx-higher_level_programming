#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_key = None
    best_score = None

    for key, score in a_dictionary.items():
        if best_score is None or score > best_score:
            best_score = score
            best_key = key

    return best_key
