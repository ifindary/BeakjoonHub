import heapq
import sys
input=sys.stdin.readline

def jump():
    N = int(input()) # 계산 개수
    board = [list(map(int, input().split())) for _ in range(N)] #점프판

    dp = [[0]*N for _ in range(N)] # 도착 가능한 횟수
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1: # 목표 지점 도착
                break

            if i+board[i][j] < N: # 오른쪽으로 이동
                dp[i+board[i][j]][j] += dp[i][j]
            
            if j+board[i][j] < N: # 아래로 이동            
                dp[i][j+board[i][j]] += dp[i][j]

    print(dp[-1][-1])


# main
jump()