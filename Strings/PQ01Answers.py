

def shortest_len(*strings):
    """Define a function, shortest_len, that takes an arbitrary number of strings and returns the shortest length a string has within
    the arguments. >>> shortest_len("here", "there", "gone", "hfhfhfhfhf")
    4"""
    i = 1
    current = strings[0]
    while i < len(strings):
        if len(strings[i]) < len(current):
            current = strings[i]
            i += 1
        else:
            i += 1
    return len(current)