from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

q = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            q.append([graph[i][j], i, j, 0]) # 바이러스 번호, x 좌표, y 좌표, 시간

q = deque(sorted(q))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    a, x, y, t = q.popleft()
    if t >= S:
        break

    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and graph[x+dx[i]][y+dy[i]] == 0:
            graph[x+dx[i]][y+dy[i]] = a

            if t+1 < S:
                q.append([a, x+dx[i], y+dy[i], t+1])

print(graph[X-1][Y-1])