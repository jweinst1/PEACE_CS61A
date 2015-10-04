

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
    def converter(elem):
        if elem == '0':
            return 0
        elif elem == '1':
            return 1
        elif elem == '2':
            return 2
        elif elem == '3':
            return 3
        elif elem == '4':
            return 4
        elif elem == '5':
            return 5
        elif elem == '6':
            return 6
        elif elem == '7':
            return 7
        elif elem == '8':
            return 8
        elif elem == '9':
            return 9
    numbers = [str(x) for x in range(10)]
    total_symbols = numbers + ['-']
    for elem in string: #will not proceed if the string contains non int elements
        if elem not in total_symbols:
            raise ValueError("invalid literal")
    negative = False
    i = len(string)-1
    integer = 0
    place_hold_count = 1
    while 0 <= i:
        if i == 0:
            if string[i] == '0':
                raise ValueError("invalid literal")
            elif string[i] == '-':
                negative = True
                i -= 1
            else:
                integer += (converter(string[i])*place_hold_count)
                i -= 1
        elif i == len(string)-1:
            integer += converter(string[i])
            i -= 1
            place_hold_count *= 10
        else:
            if string[i] == '-':
                raise ValueError("invalid literal")
            else:
                integer += (converter(string[i])*place_hold_count)
                i -= 1
                place_hold_count *= 10
    if negative == True:
        integer -= (2*integer)
        return integer
    return integer

