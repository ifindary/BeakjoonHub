import sys
input = sys.stdin.readline

def making_dots(N):
    stars = [[' ']*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j >= N - i - 1:
                stars[i][j] = '*'

        print(''.join(stars[i]))
        

N = int(input())
making_dots(N)
