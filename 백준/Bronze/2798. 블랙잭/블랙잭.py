from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().rstrip().split()))

ans = 0

for com in combinations(cards, 3):
    temp = sum(com)

    if temp <= M and temp > ans:
        ans = temp

print(ans)