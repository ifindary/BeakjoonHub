import sys
input=sys.stdin.readline

def hotel():
    T = int(input())

    for _ in range(T):
        H, W, N = map(int, input().split())

        XX = 1

        while N > H:
            N = N-H
            XX += 1

        if XX < 10:
            print(N, '0', XX, sep='')
        else:
            print(N, XX, sep='')


# main
hotel()