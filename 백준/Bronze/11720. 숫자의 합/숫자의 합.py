import sys
input = sys.stdin.readline

N = int(input())
numbers = input().rstrip()
sum = 0

for n in numbers:
    sum += int(n)

print(sum)