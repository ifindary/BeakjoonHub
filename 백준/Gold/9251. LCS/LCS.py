import sys
input=sys.stdin.readline

def LCS():
  A = 'O'+input().rstrip() # 첫 번째 문자열
  B = 'O'+input().rstrip() # 두 번째 문자열

  l = [[0]*(len(B)) for _ in range(len(A))]

  for i in range(1, len(A)):
    for j in range(1, len(B)):
      if A[i] == B[j]:
        l[i][j] = l[i-1][j-1] + 1
      else:
        l[i][j] = max(l[i-1][j], l[i][j-1])

  print(l[len(A)-1][len(B)-1])

LCS()