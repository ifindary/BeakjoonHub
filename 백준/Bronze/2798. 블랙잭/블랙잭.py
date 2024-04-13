from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().rstrip().split()))

case = list(combinations(cards, 3))
ans = 0

for i in range(len(case)):
    temp = sum(case[i])

    if temp <= M and temp > ans:
        ans = temp

print(ans)