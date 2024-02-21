import sys
input=sys.stdin.readline

# |||
# |||     |||
# ||| ||| |||  ?
#  1   2   3   4

# 위와 같은 탑 배치가 있을 때 4번 탑에 레이저를 쏜다고 가정하자
# 4번 탑의 높이와 무관하게 2번 탑은 검사를 안 해도 된다

def top():
    N = int(input())
    tops = list(map(int,input().split()))
    ans = [0]*N
    temp = []

    for i in range(len(tops)):
        while temp:
            if tops[temp[-1][0]]<tops[i]:
                temp.pop()
            else:
                ans[i] = temp[-1][0]+1
                break
        
        temp.append((i,tops[i]))
    
    print(*ans)


top()