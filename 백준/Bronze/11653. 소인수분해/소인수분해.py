import math
import sys
input = sys.stdin.readline

N = int(input())
d = 2
sqrt = math.sqrt(N)

while d <= sqrt:
    if N % d == 0:
        print(d)
        N = N//d
    else:
        d += 1

if N > 1:
    print(N)