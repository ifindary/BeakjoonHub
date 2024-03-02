from math import sqrt
from itertools import combinations_with_replacement
import sys
input=sys.stdin.readline

def four_squares():
    N = int(input())

    squares = [i*i for i in range(1, int(sqrt(N))+1)]
    squares_two = [sum(k) for k in combinations_with_replacement(squares, 2)]

    if N in squares:
        return 1
    elif N in squares_two:
        return 2
    else:
        for square in squares:
            if N - square in squares_two:
                return 3
    
    return 4


# main
print(four_squares())