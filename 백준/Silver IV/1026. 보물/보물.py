import sys
input=sys.stdin.readline

def minmultiple():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    sortB = sorted(B)
    ans = 0

    for i in range(N):
        ans += A[i] * sortB[i]

    print(ans)


# main
minmultiple()