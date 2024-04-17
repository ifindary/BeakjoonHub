import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
vedio = list(map(int, input().rstrip().split()))

start = max(vedio)
end = sum(vedio)
ans = 0

while start <= end:
    mid = (start+end)//2

    total = 0
    cnt = 1

    for v in vedio:
        if total + v > mid:
            cnt += 1
            total = 0
        
        total += v
    
    if cnt <= M:
        ans = mid
        end = mid-1
    else:
        start = mid + 1

print(ans)