import sys
input = sys.stdin.readline

def fast_sum():
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())
        print(A+B)

# main
fast_sum()