import sys
input=sys.stdin.readline

def set_bridge():
    T = int(input())

    for _ in range(T):
        cnt = 0

        N, M = map(int, input().split())
        
        dp = [0] * (M+1)
        dp[0] = 1

        for i in range(1, M+1):
            dp[i] = dp[i-1]*i

        cnt = dp[M]//(dp[N]*dp[M-N])

        print(cnt)


# main
set_bridge()