import sys
input=sys.stdin.readline
INF = 2**31

def matrix_multiple():
  M = int(input()) # 행렬 개수

  # 행렬 값 설정
  r, c = map(int, input().split())
  matrix = [r, c]

  for _ in range(M-1):
    _, c = map(int, input().split())
    matrix.append(c)

  N = len(matrix)-1

  dp = [[0]*(N+1) for _ in range(N+1)]

  for diagonal in range(1, N):
    for i in range(1, N-diagonal+1):
      j = i + diagonal

      dp[i][j] = minimum(dp, matrix, i, j)
    
  print(dp[1][-1])

def minimum(dp, matrix, i, j):
  minValue = INF

  for k in range(i, j):
    newValue = dp[i][k]+dp[k+1][j]+matrix[i-1]*matrix[k]*matrix[j]

    if minValue > newValue:
      minValue = newValue

  return minValue


## main
matrix_multiple()

# 참고 https://www.youtube.com/watch?v=5MXOUix_Ud4