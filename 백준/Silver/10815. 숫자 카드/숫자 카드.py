import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().rstrip().split()))

M = int(input())
targets = list(map(int, input().rstrip().split()))

dict = {} # 딕셔너리

for i in range(N):
    dict[cards[i]] = 0

for i in range(M):
    if targets[i] in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')