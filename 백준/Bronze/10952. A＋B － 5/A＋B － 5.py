import sys
input = sys.stdin.readline

while True:
  A, B = map(int, input().rstrip().split())

  if A == 0 and B == 0:
    break

  print(A+B)