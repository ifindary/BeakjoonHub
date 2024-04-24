from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
steps = list(map(int, input().split()))
steps.reverse()

cards = deque()
now = 1

for step in steps:
    if step == 1:
        cards.appendleft(now)
    elif step == 2:
        cards.insert(1, now)
    elif step == 3:
        cards.append(now)

    now += 1

print(*cards)