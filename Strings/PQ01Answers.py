

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
    #>>> shortest_str('love', 'peace', 'red', 'now')
    #['red', 'now']
    shortest = shortest_len(strings)
    lst = [elem for elem in strings if len(elem) == shortest]
    if len(lst) == 1:
        return lst[0]
    else:
        return lst

def lst_to_str(lst):
    #Define a function, lst_to_str, that takes a list and joins it together as a new string.
    #>>> lst_to_str([7, 5, 'a', 4, 5, 3])
    #'75a453'
    new = ''
    for elem in lst:
        new += str(elem)
    return new

def repeat_str(char, i):
    #Define a function, repeat_str, that returns a string containing the char, repeated i times.
    new = ''
    count = 0
    while count < i:
        new += char
        count += 1
    return new

"""Challenge Problem"""
def str_to_int(string):
    #Define a function, repeat_str, that takes a string and returns the corresponding integer. You cannot use int().
    #Pay careful attention for errors, such as the possiblity of "070", which does not evaluate to an integer,
    #You must include support for negative numbers as well.
    numbers = [str(x) for x in range(10)]
    total_symbols = numbers + ['-']
    for elem in string:
        if elem not in total_symbols:
            raise ValueError("invalid literal")
    negative = False
    i = 0
    while i < len(string)-1:
        if i == 0:
            if string[i] == '0':
                raise ValueError("invalid literal")
            elif string[i] == '-':
                negative = True
                i += 1
            else:
                pass

