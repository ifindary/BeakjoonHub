import sys
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
lines = list(int(input()) for _ in range(K))

ans = 0

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(K):
        cnt += lines[i]//mid

    if cnt >= N:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)