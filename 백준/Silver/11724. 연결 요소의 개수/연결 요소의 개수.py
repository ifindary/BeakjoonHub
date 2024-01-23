import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split()) # 정점 N개, 간선 M개
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
cc = 0 # dfs를 몇 개의 그래프를 대상으로 돌렸는지 기록

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for j in range(1, N+1):
    if not visited[j]:
        cc += 1
        dfs(j)

print(cc)