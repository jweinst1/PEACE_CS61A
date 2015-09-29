

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

def shortest_str(*strings):
    #Define a function, shortest_str, that takes an arbitrary number of strings and returns the string with the shortest length.
    #If two or more strings share the shortest length, it will return a list of those strings.
    #Hint: consider using your shortest_len function.
    shortest = shortest_len(strings)
    lst = [elem for elem in strings if len(elem) == shortest]
    if len(lst) == 1:
        return lst[0]
    else:
        return lst