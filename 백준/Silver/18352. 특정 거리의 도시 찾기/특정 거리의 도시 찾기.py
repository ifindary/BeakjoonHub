import heapq
import sys
input = sys.stdin.readline
INF = 1e5 # int를 사용할 예정이라 INF를 따로 정의

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향

def dijkstra(start):
    q = []
    ans = [] # 답안 기록
    distance = [INF]*(N+1) # X에서 걸리는 최단 거리

    heapq.heappush(q, (0, start)) # 거리(우선 순위), 값
    distance[start] = 0 # 출발 도시 X에서 X로 가는 최단 거리는 항상 0

    while q:
        d, now = heapq.heappop(q)

        if distance[now] < d: # 원래 거리보다 멀면 넘기기(= 이미 방문했다)
            continue

        if distance[now] == K: # 1씩 멀어질 거라 지금 K면 추가로 계산할 필요 없음
            ans.append(now)
            continue

        for i in graph[now]:
            if d + 1 < distance[i]:
                distance[i] = d + 1
                heapq.heappush(q, (d+1, i))

    if ans:
        print(*ans, sep='\n')
    else:
        print(-1)


dijkstra(X) # 함수 실행