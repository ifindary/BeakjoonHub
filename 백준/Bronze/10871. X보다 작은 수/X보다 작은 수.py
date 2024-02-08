import sys
input=sys.stdin.readline

def is_min():
    N, X = map(int, input().split())

    numbers = list(map(int, input().split()))
    ans = []

    for a in numbers:
        if a < X:
            ans.append(a)

    print(*ans)


# main
is_min()