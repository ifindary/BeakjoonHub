from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # 1~N-1: 기본/중간 부품, N 완제품
M = int(input()) # 부품간의 관계
parts = [[] for _ in range(N+1)]

indegree = [0]*(N+1) # 진입 차수
total_cnt = [0]*(N+1) # 필요 부품 수

for _ in range(M):
    # x를 만드는데 기본/중간 부품 Y가 K개 필요
    x, y, k = map(int, input().split())
    parts[x].append([y, k])
    indegree[y] += 1

q = deque()
q.append(N)

while q:
    now = q.popleft()

    if parts[now]:
        for part, cnt in parts[now]:
            indegree[part] -= 1
            
            if total_cnt[now] == 0:
                total_cnt[part] += cnt
            else:
                total_cnt[part] += cnt*total_cnt[now]

            if not indegree[part]:
                q.append(part)
    
        total_cnt[now] = 0        
    
for i in range(len(total_cnt)):
    if total_cnt[i]:
        print(i, total_cnt[i])