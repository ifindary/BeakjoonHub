import sys
input = sys.stdin.readline

M = int(input())
S = [0] * 21

for _ in range(M):
  command = list(input().rstrip().split())

  if command[0] == 'add':
    if S[int(command[1])] == 0:
      S[int(command[1])] = 1
  elif command[0] == 'remove':
    S[int(command[1])] = 0
  elif command[0] == 'check':
    if S[int(command[1])]:
      print(1)
    else:
      print(0)
  elif command[0] == 'toggle':
    if S[int(command[1])]:
      S[int(command[1])] = 0
    else:
      S[int(command[1])] = 1
  elif command[0] == 'all':
    S = [1] * 21
  elif command[0] == 'empty':
    S = [0] * 21