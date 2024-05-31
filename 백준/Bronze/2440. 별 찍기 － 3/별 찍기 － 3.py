import sys
input = sys.stdin.readline

def stars(N: int):
    for i in range(N, 0, -1):
        print('*'*i)

N = int(input())
stars(N)