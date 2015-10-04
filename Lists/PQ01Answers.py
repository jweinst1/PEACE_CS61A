__author__ = 'Josh'

def merge_all(*lsts):
    #Define a function, merge_all, which takes an arbitrary number of lists an merges them into one.
    new = []
    for elem in lsts:
        new += elem
    return new

def prime_range(n):
    #Return a list of prime numbers up to n. Try doing this using list comprehensions.
    def is_prime(n):
        for i in range(2, n):
            if n%i==0:
                return False
        return True
    return [elem for elem in range(n) if is_prime(elem)]

def parse_str(lst):
    #Define a function, parse_str, that takes a lst of integers, and returns a list of the corresponding strings to those
    #integers.
    return [str(elem) for elem in lst if type(elem) == int]

def partition_to_lst(lst):
    #Define a function, partition_to_lst that takes a list and returns a list of lists where
    #Where each element in the original list is inside a new list.
    #NOTE: elements in lst should not be split up, such as strings. The list() function might not work
    #exactly how you want it to.
    return [[elem] for elem in lst]

def str_to_lst(string):
    #Define a function, str_to_lst, that takes a string and returns a list of each individual character in the string.
    #You cannot use the list() function here.
    size = len(string)-1
    newlist = []
    for i in range(size):
        newlist.append(string[i])
    return newlist

def addition_pairs(n):
    #Define a function, addition_pairs, that returns a tuple of lists, where the two integers in each tuple add up to n.
    #Your list must contain all possible n-permutations, meanign the order does matter between numbers.
    return [(x, y) for x in range(n) for y in range(n) if x + y == n]