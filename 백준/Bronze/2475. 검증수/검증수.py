import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))

temp = 0

for i in range(0, 5):
    temp += numbers[i]**2

ans = temp%10

print(ans)