import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # RecursionError 방지

N, M = map(int, input().split()) # N 학생 수, M 힌트
graph = [[] for _ in range(N+1)] # 대상:[선행 조건] 형태
line = [] # 줄을 선 순서
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a) # b가 줄을 서려면 a가 먼저 서야 한다

def dfs(v):
    if visited[v] == True: # 이미 방문한 노드면 넘기기
        return
    
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

    # 여기까지 왔으면 이제 줄을 서도 된다는 뜻
    line.append(v)

for i in range(1, N+1):
    dfs(i)

print(*line)