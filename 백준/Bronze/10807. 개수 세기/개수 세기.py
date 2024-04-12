import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().rstrip().split()))
v = int(input())

print(numbers.count(v))