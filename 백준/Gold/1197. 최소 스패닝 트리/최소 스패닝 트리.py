import sys
input = sys.stdin.readline

V, E = map(int, input().split()) # 노드의 수, 간선의 수

# 부모 노드의 초기값은 자기 자신
# 인덱스 0은 사용하지 않을 거라 V+1로 설정
parent = [i for i in range(V+1)]

def find(x):
    if parent[x] != x: # 부모가 자기 자신인 경우가 아니라면
        parent[x] = find(parent[x]) # 부모 노드의 부모를 찾기
    return parent[x]

def union(a, b):
    # a와 b의 부모 노드 찾기
    a = find(a)
    b = find(b)
    # 둘 중 원소 값이 작은 노드를 부모로 정함(규칙)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0
cnt = 0

# 간선들 정렬
for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# cost 기준으로 오름차순 정렬
edges.sort()

# 크루스칼 알고리즘 수행
for cost, a, b in edges:
    if find(a) != find(b): # 둘의 부모 노드가 같지 않다면 (같으면 사이클 발생해서 안 됨)
        union(a, b)
        total_cost += cost
        cnt += 1

        if cnt == V-1:
            break

print(total_cost)