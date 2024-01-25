import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == '-':
            if j > 0 and graph[i][j-1] == '-':
                continue
            cnt += 1
        elif graph[i][j] == '|':
            if i > 0 and graph[i-1][j] == '|':
                continue
            cnt += 1

print(cnt)