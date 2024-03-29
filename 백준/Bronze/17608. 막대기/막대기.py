import sys
input = sys.stdin.readline

N = int(input())

sticks = [int(input()) for _ in range(N)]
ans = 1

x = sticks.pop()

while sticks:
  temp = sticks.pop()

  if  x < temp:
    ans += 1
    x = temp


print(ans)