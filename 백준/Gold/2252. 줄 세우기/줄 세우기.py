from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N 학생 수, M 힌트
graph = [[] for _ in range(N+1)] # 대상:[선행 조건] 형태
line = [] # 줄을 선 순서

indegree = [0]*(N+1) # 진입 차수

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # a가 줄을 서려면 b가 먼저 서야 한다
    indegree[b] += 1

def tepology_sort():
    line = [] # 줄을 서는 순서
    q = deque() # 줄을 설 수 있는 사람(진입 차수가 0) 

    for i in range(1, N+1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        line.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    print(*line)

tepology_sort()