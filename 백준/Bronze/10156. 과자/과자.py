import sys
input = sys.stdin.readline

def atm():
    K, N, M = map(int, input().split()) # 과자 하나의 가격, 과자 수, 보유 자금

    ans = K*N - M

    if ans > 0:
        return ans
    else:
        return 0


# main
print(atm())