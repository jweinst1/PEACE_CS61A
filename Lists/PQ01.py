__author__ = 'Josh'

def merge_all(*lsts):
    #Define a function, merge_all, which takes an arbitrary number of lists an merges them into one.
    pass

def prime_range(n):
    #Return a list of prime numbers up to n. Try doing this using list comprehensions.
    #>>> prime_range(50)
    #[0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    pass

def parse_str(lst):
    #Define a function, parse_str, that takes a lst of integers, and returns a list of the corresponding strings to those
    #integers. Consider the possibility that you may have non-integer elements in the list.
    #>>> parse_str([6, 5, 4, 33, 24])
    #['6', '5', '4', '33', '24']
    #>>> parse_str([6, 5, 4, 'art', 'buzz'])
    #['6', '5', '4']
    #>>> parse_str([1, [5], '[[][', 4])
    #['1', '4']
    pass

def partition_to_lst(lst):
    #Define a function, partition_to_lst that takes a list and returns a list of lists where
    #Where each element in the original list is inside a new list.
    #NOTE: elements in lst should not be split up, such as strings. The list() function might not work
    #exactly how you want it to.
    #>>> partition_to_lst(['howis', 4, 66, 789])
    #[['howis'], [4], [66], [789]]
    pass

def str_to_lst(string):
    #Define a function, str_to_lst, that takes a string and returns a list of each individual character in the string.
    #You cannot use the list() function here.
    #>>> str_to_lst("How are you today?")
    #['H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 't', 'o', 'd', 'a', 'y']
    #>>> str_to_lst("Do not overdose on billaldehyde.")
    #['D', 'o', ' ', 'n', 'o', 't', ' ', 'o', 'v', 'e', 'r', 'd', 'o', 's', 'e', ' ', 'o', 'n', ' ', 'b', 'i', 'l', 'l', 'a', 'l', 'd', 'e', 'h', 'y', 'd', 'e']
    pass

def addition_pairs(n):
    #Define a function, addition_pairs, that returns a tuple of lists, where the two integers in each tuple add up to n.
    #Your list must contain all possible n-permutations, meanign the order does matter between numbers.
    pass