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
