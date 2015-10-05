
def index_int(num, i):
    #Define a function, index_int, where you input an integer, and a selection, i, and return the ith index
    #of the integer.
    return int(str(num)[i])

def pop_int(num):
    #Define a function, pop_int, where you remove the last digit of an integer. Meaning 544 becomes 54. If the integer is
    #a single digit, raise a ValueError.
    if len(str(num)) == 1:
        raise ValueError("Integer is too small")
    else:
        num = (num - num%10)//10
        return num
