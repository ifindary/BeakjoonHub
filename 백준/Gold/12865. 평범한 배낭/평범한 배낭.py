import sys
input=sys.stdin.readline

def Knapsack():
  N, K = map(int, input().split()) # 물품의 수, 버틸 수 있는 무게
  items = [(0,0)]
  dp = [[0]*(K+1) for _ in range(N+1)]
  total_weight = 0
  total_value = 0

  for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V)) # 무게, 가치
    total_weight += W
    total_value += V

  if total_weight <= K:
    print(total_value)
  else:
    for i in range(1, N+1):
      for j in range(1, K+1):
        if items[i][0] > j:
          dp[i][j] = dp[i - 1][j]
        else:
          dp[i][j] = max(dp[i-1][j], items[i][1] + dp[i - 1][j - items[i][0]])
  
    print(dp[N][K])


Knapsack()