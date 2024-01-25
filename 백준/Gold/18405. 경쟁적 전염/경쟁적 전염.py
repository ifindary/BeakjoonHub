from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = [input().rstrip().split() for _ in range(N)]
S, X, Y = map(int, input().split())

graph = [[0]*N for _ in range(N)]

q = deque()

# temp를 바로 int로 받는 법이 기억 안 나서 임시 처리
for i in range(N):
    for j in range(N):
        graph[i][j] = int(temp[i][j])

        if graph[i][j] != 0:
            q.append([graph[i][j], i, j])

q = deque(sorted(q))

now = 0
wait = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


while now < S:
    while q:
        temp = q.popleft()

        a = temp[0]
        x = temp[1]
        y = temp[2]

        # a: 지금 탐색 중인 바이러스. x, y: 현재 탐색 중인 위치
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and graph[x+dx[i]][y+dy[i]] == 0:
                graph[x+dx[i]][y+dy[i]] = a
                wait.append([a, x+dx[i], y+dy[i]])

    while wait:
        q.append(wait.popleft())

    now += 1


print(graph[X-1][Y-1])