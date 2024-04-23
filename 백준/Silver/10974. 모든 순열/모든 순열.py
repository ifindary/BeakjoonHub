from itertools import permutations
import sys
input = sys.stdin.readline

A = list(int(i+1) for i in range(int(input())))

for B in permutations(A, len(A)):
    print(*B)