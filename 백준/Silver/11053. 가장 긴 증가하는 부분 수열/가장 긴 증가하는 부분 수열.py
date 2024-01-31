import sys
input=sys.stdin.readline

def LIS():
  N = int(input()) # 수열의 크기
  array = list(map(int, input().split()))
  
  dp = [1]*N # 길이는 무조건 1 이상

  for i in range(1, N):
    for j in range(i):
      if array[i] > array[j]:
        dp[i] = max(dp[i], dp[j]+1)

  print(max(dp))


LIS()