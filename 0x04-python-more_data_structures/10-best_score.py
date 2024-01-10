#!/usr/bin/python3
best_key = None
best_score = None

for key, score in a_dictionary.items():
    if best_score is None or score > best_score:
        best_score = score
        best_key = key

return best_key
