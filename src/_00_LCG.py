
from time import time

def LCG(lower_limit : int, upper_limit : int) -> int:
    """
    membuat angka random dengan rentang lower_limit-upper_limit
    """    
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(time())
    seed = (a*seed + c) % m
    while seed % (upper_limit + 1) < lower_limit:
        seed = (a*seed + c) % m
    return seed % (upper_limit + 1)

if __name__ == '__main__':
    LCG()
    
