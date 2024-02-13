import sys
input=sys.stdin.readline

def wifi():
    N, C = map(int, input().split())
    house = [int(input()) for _ in range(N)]
    house.sort()

    start = 1 # 최소 거리
    end = house[-1] - house[0] # 최대 거리
    ans = 0

    while start <= end:
        cnt = 1
        distance = (start+end)//2

        now = 0
        
        for i in range(1, N):
            if house[i]-house[now] >= distance:
                cnt += 1
                now = i
        
        if cnt >= C:
            start = distance+1
            ans = distance
        else:
            end = distance-1

    print(ans)


# main
wifi()