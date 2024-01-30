import sys
input=sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

def count(coins, M):
  dp = [0]*(M+1) # 결과를 저장할 테이블
  dp[0] = 1

  for coin in coins:
    for i in range(coin, M+1):
      dp[i] += dp[i-coin]

  print(dp[M])


for _ in range(T):
  N = int(input()) # 동전 가지 수
  coins = list(map(int, input().split())) # 동전 금액
  M = int(input()) # 만들어야 할 금액

  count(coins, M)