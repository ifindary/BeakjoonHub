import sys
input = sys.stdin.readline

def atm():
    N = int(input()) # 사람 수
    wating = list(map(int, input().split())) # 대기 시간

    wating.sort()

    ans = [0]

    for time in wating:
        ans.append(ans[-1]+time)

    return sum(ans)


# main
print(atm())