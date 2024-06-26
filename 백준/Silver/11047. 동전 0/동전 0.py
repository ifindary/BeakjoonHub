import sys
input = sys.stdin.readline

# 동전 문제. 그리고 상위 동전은 하위 동전의 배수니까 그리디 알고리즘 사용 가능.

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0

for coin in reversed(coins):
    if K // coin:
        cnt += K//coin
        K %= coin

print(cnt)