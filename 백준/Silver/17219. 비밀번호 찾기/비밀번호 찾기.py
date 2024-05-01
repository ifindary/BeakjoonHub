import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dict = {}

for _ in range(N):
    site, password = input().rstrip().split()
    dict[site] = password

for _ in range(M):
    print(dict[input().rstrip()])