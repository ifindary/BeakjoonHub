from collections import deque
import sys
input=sys.stdin.readline

def ioioi():
    N = int(input())
    M = int(input())
    S = input().rstrip()

    P = 'IO'*N + 'I'
    ans = 0

    for i in range(M-len(P)+1):
        if S[i:i+len(P)] == P:
            ans += 1

    print(ans)


# main
ioioi()