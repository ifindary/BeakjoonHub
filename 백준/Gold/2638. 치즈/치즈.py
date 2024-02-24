from collections import deque
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
q = deque()


def cheese_time():
    day = 0         
    
    while True:
        bfs()

        for i in range(N):
            for j in range(M):
                if cheese[i][j] >= 3:
                    cheese[i][j] = 0
                elif cheese[i][j] == 2:
                    cheese[i][j] = 1

        day += 1

        if all(all(element == 0 for element in row) for row in cheese):
            break
        
    print(day)


def bfs():
    visited = [[0]*M for _ in range(N)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[0][0] = 1
    q.append([0,0])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < M and not visited[nx][ny]:
                if cheese[nx][ny] > 0:
                    cheese[nx][ny] += 1
                
                else:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

cheese_time()