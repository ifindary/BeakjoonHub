import sys
input=sys.stdin.readline

def factorial(N):
    dp = [0] * (N+1)
    dp[0] = 1

    for i in range(1, N+1):
        dp[i] = dp[i-1]*i
    
    return dp[N]

# find : 부모 찾기
def set_bridge():
    T = int(input())

    for _ in range(T):
        cnt = 0

        N, M = map(int, input().split())
        
        cnt = factorial(M)//(factorial(N)*factorial(M-N))

        print(cnt)


# main
set_bridge()