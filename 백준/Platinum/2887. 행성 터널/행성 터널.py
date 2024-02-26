import sys
input=sys.stdin.readline

# 초기값 설정
N = int(input()) # 행성의 개수
planets = [] # 행성별 비용
costs = [] # 터널 비용 목록
parent = [] # 부모 목록

for i in range(N):
    x, y, z =  map(int, input().split())
    planets.append((x, y, z, i)) # i = 행성 번호
    parent.append(i) # 초기 부모는 자기 자신

#####

# find : 부모 찾기
def find(parent:list, x:int):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union : 부모를 같게 만들기
def union(parent:list, x:int, y:int):
    x = find(parent, x)
    y = find(parent, y)

    if x < y: # 둘 중 작은 쪽이 부모가 되도록 갱신
        parent[y] = x
    else:
        parent[x] = y
    
# 크루스칼 알고리즘을 이용한 행성 터널 계산
def planet_tunnel():
    for i in range(3):
        planets.sort(key=lambda x: x[i]) # 가장 차이가 적은 값끼리만 비교

        for j in range(1, N):
            costs.append((planets[j][3], planets[j-1][3], abs(planets[j][i]-planets[j-1][i])))


    costs.sort(key=lambda x:x[2])
    total_cost = 0 # 총 비용
    cnt = 0 # 연결된 수
    
    for i in range(len(costs)):
        a, b, cost = costs[i]

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            cnt += 1

        if cnt >= N-1: # 모든 노드가 연결되었으면 탐색 종료
            break

    print(total_cost)


# main
planet_tunnel()