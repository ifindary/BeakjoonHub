from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dfs_ans = []
bfs_ans = []

for _ in range(M):
    a, b  = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

for neighbors in graph:
    neighbors.sort()

def dfs(v):
    visited[v] = True
    dfs_ans.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)

    visited[v] = True

    while q:
        x = q.popleft()
        bfs_ans.append(x)

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

dfs(V)
print(*dfs_ans)

visited = [False] * (N+1)

bfs(V)
print(*bfs_ans)