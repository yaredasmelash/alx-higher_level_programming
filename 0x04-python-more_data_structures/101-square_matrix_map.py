#!/usr/bin/python3
def square_matrix_(matrix):
    return (list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix)))
