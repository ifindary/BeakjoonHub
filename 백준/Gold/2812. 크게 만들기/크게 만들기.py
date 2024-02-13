import sys
input=sys.stdin.readline

def makebig():
    N, K = map(int, input().split())
    A = input().rstrip()
    temp = []

    for i in range(N):
        while K > 0 and temp and int(A[i]) > temp[-1]:
            temp.pop()
            K -=1
        
        temp.append(int(A[i]))
    
    for i in range(len(temp)-K):
        print(temp[i], end='')


# main
makebig()