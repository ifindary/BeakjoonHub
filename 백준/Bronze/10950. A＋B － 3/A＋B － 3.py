import sys
input=sys.stdin.readline

def plus():
    T = int(input()) # 테스트 케이스의 개수

    for _ in range(T):
        A, B = map(int, input().split())

        print(A+B)

# main
plus()