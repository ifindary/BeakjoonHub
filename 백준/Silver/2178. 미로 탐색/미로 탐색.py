from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]  # 2차원 리스트로 변환

q = deque()
q.append((0, 0, 1))

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 dx, dy 배열
dy = [0, 0, -1, 1]

while q:
    x, y, cost = q.popleft()

    if x == N - 1 and y == M - 1:
        print(cost)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
            q.append((nx, ny, cost + 1))
            maze[nx][ny] = 0  # 방문한 곳은 0으로 표시하여 중복 방문 방지