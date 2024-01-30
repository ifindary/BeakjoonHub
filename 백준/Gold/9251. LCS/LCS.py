import sys
input=sys.stdin.readline

def LCS():
  A = input().rstrip() # 첫 번째 문자열
  B = input().rstrip() # 두 번째 문자열

  l = [0]*(len(B))

  for a in A:
    cnt = 0
    for i, b in enumerate(B): # 인덱스, 문자열
      if cnt < l[i]:
        cnt = l[i]
      elif a == b:
        l[i] = cnt+1

  print(max(l))

LCS()