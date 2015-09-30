__author__ = 'Josh'

def merge_all(*lsts):
    #Define a function, merge_all, which takes an arbitrary number of lists an merges them into one.
    new = []
    for elem in lsts:
        new += elem
    return new
