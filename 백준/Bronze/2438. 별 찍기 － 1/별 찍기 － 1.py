import sys
input = sys.stdin.readline

def stars():
    N = int(input())    

    for i in range(N):
        print('*'*(i+1))

# main
stars()