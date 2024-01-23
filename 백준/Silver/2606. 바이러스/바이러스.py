import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
e = int(input()) # 연결된 컴퓨터의 수

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True)-1) # 1번은 제외