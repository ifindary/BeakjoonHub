import sys
input = sys.stdin.readline

N = int(input())

a = 1
b = 1

for _ in range(2, N+1):
    a, b = b, (a + b)%15746

print(b)