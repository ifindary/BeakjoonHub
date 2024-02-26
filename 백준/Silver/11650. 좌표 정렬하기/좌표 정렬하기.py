import sys
input=sys.stdin.readline

def sorting():
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    numbers.sort()

    for i in range(N):
        print(*numbers[i])

# main
sorting()