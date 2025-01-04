import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

new_score = sum(score)/N / max(score)*100

print(new_score)