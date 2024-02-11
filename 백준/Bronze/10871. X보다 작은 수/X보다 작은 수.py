import sys
input=sys.stdin.readline

def is_less():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []

    for a in A:
        if a < X:
            ans.append(a)

    print(*ans)


# main
is_less()