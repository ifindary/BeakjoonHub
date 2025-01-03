import math
import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    score = 0
else:
    opinions = []

    for _ in range(n):
        opinions.append(int(input()))

    a = math.floor(n*0.15 + 0.5)

    if a == 0:
        score = math.floor(sum(opinions) / len(opinions) + 0.5)
    else:
        opinions.sort()
        new_op = opinions[a:-a]
        score = math.floor(sum(new_op) / len(new_op) + 0.5)

print(score)