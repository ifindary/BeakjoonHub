import sys
input = sys.stdin.readline

N = int(input())

a = 1
b = 1

for _ in range(3, N+1):
    a, b = b%15746, (a + b)%15746

if N == 1:
    print(1)
else:
    print((a + b)%15746)